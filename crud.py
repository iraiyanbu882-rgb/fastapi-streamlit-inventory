from sqlalchemy.orm import Session
import models
import schema

def create_products(db:Session,product:schema.ProductCreate):
    db_product=models.product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_products(db:Session):
    return db.query(models.product).all()

def create_sales(db:Session,sales:schema.SalesCreate):
    product=db.query(models.product).filter(
        models.product.name==sales.product_name
    ).first()

    if not product:
        return None
    if product.quantity<sales.quantity:
        return "not enough stock"
    
    total=product.price*sales.quantity
    product.quantity-=sales.quantity

    db_sale=models.sales(
        product_name=product.name,
        quantity=sales.quantity,
        total_price=total
    )

    db.add(db_sale)
    db.commit()
    db.refresh(db_sale)

    return db_sale
def get_sales(db:Session):
    return db.query(models.sales).all()