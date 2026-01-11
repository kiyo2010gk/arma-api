from pydantic import BaseModel
from typing import List

class Product(BaseModel):
    barcode: str
    name: str
    category: str
    price: float

class InventoryItem(BaseModel):
    barcode: str
    name: str
    category: str
    price: float
    balance: int
