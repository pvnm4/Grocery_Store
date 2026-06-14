from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    description: str
    unit_name: str
    price_per_unit: float
    quantity: int

    class Config:
        orm_mode = True

class ProductResponse(BaseModel):
    id: int
    name: str
    unit_name: str
    price_per_unit: float


    class Config:
        orm_mode = True

class ProductCreate(BaseModel):
    name: str
    description: str
    unit_name: str
    price_per_unit: float
    quantity: int

class Unit(BaseModel):
    id: int
    unit_name: str

    class Config:
        from_attributes = True