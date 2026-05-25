import streamlit as st
import pandas as pd
import requests

api_url='http://127.0.0.1:8000'
st.set_page_config(
    page_title='Inventory Billing System',
    layout="wide"
)

st.title("Inventory & Billing System")

menu=st.sidebar.selectbox(
    'Menu',
    [
        'dashboard',
        'Add product',
        'View Product',
        'Create Bill',
        'Sales History'
    ]
)

if menu=='dashboard':
    product=requests.get(f'{api_url}/products').json()
    sale=requests.get(f'{api_url}/sales').json()
    total_product=len(product)
    total_sales=len(sale)

    toatl_revenue=sum(s['total_price'] for s in sale)

    col1,col2,col3=st.columns(3)
    col1.metric("product",total_product)
    col1.metric("sales",total_sales)
    col1.metric("revenue",toatl_revenue)
if menu=='Add product':
    st.subheader("Add product")
    name=st.text_input("product name")
    category=st.text_input("category name")
    price=st.text_input("product price")
    quantity=st.text_input("quantity")

    if st.button("add product"):
        data={
            'name':name,
            'category':category,
            'price':price,
            'quantity':quantity
        }
        response=requests.post(f'{api_url}/products',json=data)
        st.success("product added successfully")
if menu=='View Product':
    st.subheader("Inventory")
    products=requests.get(f'{api_url}/products').json()
    df=pd.DataFrame(products)
    st.dataframe(df)

if menu=='Create Bill':
    st.subheader("Billing")
    products=requests.get(f'{api_url}/products').json()
    product_name=[p['name'] for p in products]

    select_product=st.selectbox(
        "select product",
        product_name
    )

    quantity=st.number_input('Quantity',min_value=1)

    if st.button("Generate Bill"):
        data={
            'product_name':select_product,
            'quantity':quantity
        }
        response=requests.post(f'{api_url}/sales',json=data)
        st.success("Bill Generated")

        st.json(response.json())

if menu=='Sales History':
    st.subheader("Sales")
    sale=requests.get(f'{api_url}/sales').json()
    df=pd.DataFrame(sale)
    st.dataframe(df)
