from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Product(Base):
    __tablename__ = 'products'

    product_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    unit_name = Column(String, nullable=False)  # This field is added to store the unit name directly
    # dsescription = Column(String, nullable=True)
    # unit_id = Column(Integer, ForeignKey('units.unit_id', ondelete='CASCADE'), nullable=False)
    price_per_unit = Column(Float, nullable=False)

    # unit = relationship("Unit", back_populates="products")


# class Unit(Base):
#     __tablename__ = 'units'

#     unit_id = Column(Integer, primary_key=True, index=True)
#     unit_name = Column(String, nullable=False, unique=True)

#     products = relationship("Product", back_populates="unit", cascade="all, delete-orphan")







