from sqlalchemy import Column,Integer,String,Float,DateTime
from db import Base
from datetime import datetime

class product(Base):
    __tablename__='product'
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,unique=True)
    category=Column(String)
    price=Column(Float)
    quantity=Column(Integer)
class sales(Base):
    __tablename__='sales'
    id=Column(Integer,primary_key=True,index=True)
    product_name=Column(String)
    total_price=Column(Float)
    quantity=Column(Integer)
    time=Column(DateTime,default=datetime.utcnow)