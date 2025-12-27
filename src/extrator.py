import pdfplumber
import re
from datetime import datetime
from typing import List, Optional
from .modelos import Invoice, InvoiceItem

class PDFExtrator:
    def extract_data(self, pdf_path: str) -> Optional[Invoice]:
        try:
            with pdfplumber.open(pdf_path) as pdf:
                page = pdf.pages[0]
                text = page.extract_text() or ""

                if not text:
                    return None
                # Procurar por Order ID
                order_id_match = re.search(r'(?:Order|Invoice)\s*(?:ID|#)?[:\s]+(\d+)', text, re.IGNORECASE)
                # Procurar por Date
                date_match = re.search(r'(?:Order\s*)?Date[:\s]+([\d/-]+)', text, re.IGNORECASE)
                # Procurar por Customer ID
                customer_id_match = re.search(r'Customer(?: ID)?[:\s]+(\w+)', text, re.IGNORECASE)

                if not (order_id_match and date_match and customer_id_match):
                    print(f"Falha ao extrair dados de {pdf_path}")
                    return None
                
                # Conversão de Tipos:
                order_id = int(order_id_match.group(1))
                customer_id = customer_id_match.group(1)
                date_str = date_match.group(1).strip()

                # Converter a data para o formato date
                invoice_date = None
                for fmt in ["%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y", "%d-%m-%Y"]:
                    try:
                        invoice_date = datetime.strptime(date_str, fmt).date()
                        break
                    except ValueError:
                        continue
                
                # Extrair Itens da Fatura
                items = []
                tables = page.extract_tables()

                target_tables = [t for t in tables if len(t[0]) >= 4]

                for table in target_tables:
                    for row in table:
                        if not row or len(row) < 4:
                            continue
                        
                        # Pular cabeçalhos
                        if "Product Name" in str(row[1]):
                            continue

                        # Pular rodapé
                        if "Total" in str(row[2]) or "Total" in str(row[0]):
                            continue

                        try:
                            prod_name = str(row[1]).replace('\n', ' ')

                            qty_str = str(row[2])
                            price_str = str(row[3])

                            # Limpar e converter quantidade
                            qty = int(float(qty_str))
                            price = float(price_str.replace('$', '').replace('R$', '').replace(',', '.'))

                            items.append(InvoiceItem(
                                product_name = prod_name,
                                quantity = qty,
                                unit_price = price
                            ))
                        except (ValueError, IndexError):
                            continue

                if not items:
                    print(f"Nenhum item extraído de {pdf_path}")
                    return None
                
                return Invoice(
                    order_id = order_id,
                    date = invoice_date,
                    customer_id = customer_id,
                    items = items
                )
        
        except Exception as e:
            print(f"Erro ao processar {pdf_path}: {e}")
            return None


