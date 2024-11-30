import contextlib
from typing import AsyncIterator, Optional
from sqlalchemy.ext.asyncio import (
    AsyncConnection,
    async_sessionmaker,
    create_async_engine,
)
from src.config import get_db_url


class DatabaseSessionService:
    def __init__(self,echo: bool = False):
        self.engine = create_async_engine(
            url=get_db_url(),
            echo=echo
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
        )
        
        
    async def close(self) -> None:
        if self._engine is None:
            return
        await self._engine.dispose()
        self._engine = None
        self._sessionmaker = None


    @contextlib.asynccontextmanager
    async def session(self):
        async with self._sessionmaker() as session:
            try:
                yield session
            except Exception as _ex:
                await session.rollback()
                raise _ex


    @contextlib.asynccontextmanager
    async def connect(self) -> AsyncIterator[AsyncConnection]:
        if self._engine is None:
            raise IOError("DatabaseSessionManager is not initialized")
        async with self._engine.begin() as connection:
            try:
                yield connection
            except Exception as _ex:
                await connection.rollback()
                raise _ex


db_session = DatabaseSessionService(echo=True)


async def get_session():
    async with db_session.session() as session:
        yield session