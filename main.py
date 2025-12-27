import os
import glob
from src.extrator import PDFExtrator
from src.database import DatabaseManager
from src.analises import Analises


PDF_DIR = "data" 

def main():

    # Extração de Dados
    extrator = PDFExtrator()
    manager = DatabaseManager()
    
    pdf_files = glob.glob(os.path.join(PDF_DIR, "*.pdf"))
    new_invoices = []

    if not pdf_files:
        print(f"Nenhum arquivo PDF encontrado na pasta '{PDF_DIR}'.")
    else:
        for pdf_file in pdf_files:
            print(f"Processando: {pdf_file}")
            invoice = extrator.extract_data(pdf_file)
            if invoice:
                new_invoices.append(invoice)
    
    # Armazenamento de Dados
    if new_invoices:
        manager.save_invoices(new_invoices)
    else:
        print("Nenhuma fatura válida extraída.")

    # Análise de Dados
    analytics = Analises()
    analytics.run_report()

if __name__ == "__main__":
    main()