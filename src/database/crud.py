from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.database.orm import DatabaseSessionService
from src.database.models import Winter , Summer
from fastapi import HTTPException , status


class CRUD(DatabaseSessionService):
    def __init__(self) -> None:
        super().__init__()
        self.init()
        
        
    async def create_data(self,data):
        async with self.session() as session:
            session.add(data)
            await session.commit()
            await session.refresh(data)
        return HTTPException(status_code=status.HTTP_200_OK)
    
    
    async def read_data(self,data) -> list:
        stmt = select(data).order
        
        
    