import pandas as pd
import json
import os

DB_FILE = "database.json"

class Analises:
    def run_report(self):
        # Verificar se o arquivo existe para testes
        if not os.path.exists(DB_FILE):
            print(f"Arquivo '{DB_FILE}' não encontrado.")
            return

        # Carregar dados do JSON
        try:
            with open(DB_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except json.JSONDecodeError:
            print("Erro")
            return
        
        if not data:
            print("Database vazio")
            return

        # Preparar DataFrame de Itens
        items_list = []
        for entry in data:
            order_id = entry.get('order_id')
            items = entry.get('items', [])
            
            for item in items:
                # Adicionar order_id a cada item 
                item['order_id'] = order_id
                items_list.append(item)
        
        if not items_list:
            print("Nenhum item de produto encontrado nas faturas.")
            return

        df_items = pd.DataFrame(items_list)

        # Converter colunas para tipos numéricos
        df_items['quantity'] = pd.to_numeric(df_items['quantity'], errors='coerce').fillna(0)
        df_items['unit_price'] = pd.to_numeric(df_items['unit_price'], errors='coerce').fillna(0)

        # Calcular total por linha
        df_items['total_line'] = df_items['quantity'] * df_items['unit_price']
        
        # Calcular total por fatura
        total_por_invoice = df_items.groupby('order_id')['total_line'].sum()

        # Relatório
        print("\n Relatório de Faturamento:")

        # Média do valor das faturas
        media = total_por_invoice.mean()
        print(f"Média do valor das faturas: R$ {media:.2f}")

        # Produto mais vendido (Moda)
        if not df_items.empty:
            top_prod = df_items['product_name'].mode()[0]
            print(f"Produto mais vendido: {top_prod}")

            # Faturamento por Produto (ranking dos 5)
            print("\n Faturamento por Produto (Top 5):")
            print(df_items.groupby('product_name')['total_line'].sum().sort_values(ascending=False).head(5).to_string())

            # Tabela de Preços de Produtos (Unitário)
            print("\n Tabela de Preços:")
            print(df_items[['product_name', 'unit_price']].drop_duplicates().sort_values('product_name').head(10).to_string(index=False))