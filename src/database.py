import json
import os
from typing import List
from .modelos import Invoice

DB_FILE = 'database.json'

class DatabaseManager:
    def __init__(self, db_file=DB_FILE):
        self.db_file = db_file

    def load_data(self) -> List[dict]:
        # Carrega os dados existentes ou retorna uma lista vazia se o arquivo não existir
        if not os.path.exists(self.db_file):
            return []
        try:
            with open(self.db_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
        
    def save_invoices(self, new_invoices: List[Invoice]):
        # Deduplicação nas faturas 
        existing_data = self.load_data()

        # Cria um set com os IDs existentes
        existing_ids = {item['order_id'] for item in existing_data}

        added_count = 0
        for invoice in new_invoices:
            # Order ID como chave única
            if invoice.order_id not in existing_ids:
                invoice_dict = invoice.model_dump()
                invoice_dict['date'] = invoice.date.isoformat()  # Converter date para string
                existing_data.append(invoice_dict)
                existing_ids.add(invoice.order_id)
                added_count += 1

        # Salvar os dados atualizados de volta no arquivo
        with open(self.db_file, 'w', encoding='utf-8') as f:
            json.dump(existing_data, f, ensure_ascii=False, indent=4)

        print(f"Banco de dados atualizado.")