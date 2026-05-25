from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
import schema
import crud
from db import engine,session,Base
Base.metadata.create_all(bind=engine)

app=FastAPI()

def get_db():
    db=session()
    try:
        yield db
    finally:
        db.close()

@app.post("/products")
def add_product(product:schema.ProductCreate,db:Session=Depends(get_db)):
    return crud.create_products(db,product)

@app.get("/products")
def get_products(db:Session=Depends(get_db)):
    return crud.get_products(db)
        
@app.post("/sales")
def create_sale(sale:schema.SalesCreate,db:Session=Depends(get_db)):
    return crud.create_sales(db,sale)

@app.get("/sales")
def get_sales(db:Session=Depends(get_db)):
    return crud.get_sales(db)