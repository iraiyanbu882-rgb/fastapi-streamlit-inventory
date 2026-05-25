from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

database='sqlite:///./inventory.db'

engine=create_engine(
    database,
    connect_args={'check_same_thread':False}
)

session=sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base=declarative_base()