from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/products",
    tags=['Products']
)

@router.get("/", response_model=list[schemas.ProductResponse])
def get_products(db: Session = Depends(get_db)):
    products = db.query(models.Product).all()
    return products


@router.get("/{id}", response_model=schemas.ProductResponse)
def get_product(id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.product_id == id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with id {id} not found")
    return product


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ProductResponse)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = models.Product(
        name=product.name,
        unit_name=product.unit_name,
        # unit_id=db.query(models.Unit).filter(models.Unit.unit_name == product.unit_name).first().unit_id,
        price_per_unit=product.price_per_unit
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@router.put("/{id}", response_model=schemas.ProductResponse)
def update_product(id: int, product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = db.query(models.Product).filter(models.Product.product_id == id).first()
    if not db_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with id {id} not found")
    
    db_product.name = product.name
    db_product.unit_name = product.unit_name
    # db_product.unit_id = db.query(models.Unit).filter(models.Unit.unit_name == product.unit_name).first().unit_id
    db_product.price_per_unit = product.price_per_unit

    db.commit()
    db.refresh(db_product)
    return db_product

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(models.Product).filter(models.Product.product_id == id).first()
    if not db_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with id {id} not found")
    
    db.delete(db_product)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)