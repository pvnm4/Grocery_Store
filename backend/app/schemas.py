from pydantic import BaseModel

class Product(BaseModel):
    name: str
    unit_name: str
    price_per_unit: float
    quantity: int

    class Config:
        orm_mode = True

class ProductResponse(BaseModel):
    product_id: int
    name: str
    unit_name: str
    price_per_unit: float


    class Config:
        orm_mode = True

class ProductCreate(BaseModel):
    name: str
    unit_name: str
    price_per_unit: float
    quantity: int | None = None

# class Unit(BaseModel):
#     id: int
#     unit_name: str

#     class Config:
#         from_attributes = True