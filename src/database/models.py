from sqlalchemy.orm import Mapped 
from src.database.database import Base, int_pk, str_array, str_uniq, str_nullable, str_null_true


class Winter(Base):
    id: Mapped[int_pk]
    price: Mapped[int]
    brand: Mapped[str_nullable]
    product_code: Mapped[str_nullable]
    eu_code: Mapped[str_nullable]
    full_size: Mapped[str_nullable]
    size: Mapped[str_nullable]
    pattern_name: Mapped[str_nullable]
    technical_specifications: Mapped[str_nullable]
    image: Mapped[str_array]
    availability: Mapped[str_nullable]
    
    
    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id}, "
            f"first_name={self.first_name!r},"
            f"last_name={self.last_name!r})")


    def __repr__(self):
        return str(self)
    
    
class Summer(Base):
    id: Mapped[int_pk]
    price: Mapped[int]
    brand: Mapped[str_nullable]
    product_code: Mapped[str_nullable]
    eu_code: Mapped[str_nullable]
    full_size: Mapped[str_nullable]
    size: Mapped[str_nullable]
    pattern_name: Mapped[str_nullable]
    technical_specifications: Mapped[str_nullable]
    image: Mapped[str_array]
    availability: Mapped[str_nullable]
    
    
    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id}, "
            f"first_name={self.first_name!r},"
            f"last_name={self.last_name!r})")


    def __repr__(self):
        return str(self)