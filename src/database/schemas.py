from pydantic import BaseModel, Field, field_validator
from fastapi import HTTPException , status


class WinterModel(BaseModel):
    price: int  
    brand: str
    product_code: str 
    eu_code: str 
    full_size: str 
    size: str 
    pattern_name: str 
    technical_specifications: str
    image: list 
    availability: str 
    
    
class SummerModel(BaseModel):
    price: int  
    brand: str
    product_code: str 
    eu_code: str 
    full_size: str 
    size: str 
    pattern_name: str 
    technical_specifications: str
    image: list 
    availability: str 