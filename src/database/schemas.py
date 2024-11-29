from pydantic import BaseModel, Field, field_validator
from fastapi import HTTPException , status


class WinterModel(BaseModel):
    price: int = Field(...)
    brand: str = Field(...)
    product_code: str = Field(...)
    eu_code: str = Field(...)
    full_size: str = Field(...)
    size: str = Field(...)
    pattern_name: str = Field(...)
    technical_specifications: str = Field(...)
    image: list = Field(...)
    
    
class SummerModel(BaseModel):
    price: int = Field(...)
    brand: str = Field(...)
    product_code: str = Field(...)
    eu_code: str = Field(...)
    full_size: str = Field(...)
    size: str = Field(...)
    pattern_name: str = Field(...)
    technical_specifications: str = Field(...)
    image: list = Field(...)