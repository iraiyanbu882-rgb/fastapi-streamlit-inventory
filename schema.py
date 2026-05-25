from pydantic import BaseModel
from datetime import datetime

class ProductCreate(BaseModel):
    name:str
    category:str
    price:float
    quantity:int
class ProductResponse(BaseModel):
    id:int

    class config:
        orm_model=True

class SalesCreate(BaseModel):
    product_name:str
    quantity:int

class Response(BaseModel):
    id:int
    quantity:int
    total_price:float
    time:datetime

    class config:
        orm_model=True