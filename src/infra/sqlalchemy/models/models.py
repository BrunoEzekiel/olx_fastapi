from sqlalchemy import Column, Integer, String, Float, Boolean

from src.infra.sqlalchemy.config.database import Base

class Produto(Base):

    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    disponivel = Column(Boolean)
