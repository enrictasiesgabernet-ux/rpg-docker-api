from sqlalchemy import Column, Integer, String, Float
from .database import Base
 
class Player(Base):
    __tablename__ = "players"
 
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(Integer, default=1)
    type = Column(String, nullable=False)
 
 
class Enemy(Base):
    __tablename__ = "enemies"
 
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(Integer, default=1)
    type = Column(String, nullable=False)
