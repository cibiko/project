from sqlalchemy import  Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    golds = Column(Integer, unique=True, index=True )


    heroes = relationship("Hero", back_populates="hero")


class Hero(Base):
    __tablename__ = "heroes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    power= Column(Integer, index=True)
    hero_id = Column(Integer, ForeignKey("players.id"))

    hero = relationship("Player", back_populates="heroes")
