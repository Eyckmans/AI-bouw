from sqlalchemy import Column, Integer, String
from database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)

    company_name = Column(String)
    contact_name = Column(String)
    phone = Column(String)
    email = Column(String)
    address = Column(String)
    vat_number = Column(String)
