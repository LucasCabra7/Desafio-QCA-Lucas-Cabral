from pydantic import BaseModel, Field, field_validator
from typing import List
from datetime import date

# Modelo para os itens da fatura
class InvoiceItem(BaseModel):
    product_name: str
    quantity: int 
    unit_price: float

# Modelo para a fatura
class Invoice(BaseModel):
    order_id: int
    date: date
    customer_id: str
    items: List[InvoiceItem]

    # Calculo da Prioridade
    @property
    def total(self) -> float:
        return sum(item.quantity * item.unit_price for item in self.items)