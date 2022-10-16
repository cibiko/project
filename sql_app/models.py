from sqlalchemy import  Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    email = Column(String, unique=True)
    golds = Column(Integer, unique=True )


    heroes = relationship("Hero", back_populates="hero")


class Hero(Base):
    __tablename__ = "heroes"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    power= Column(Integer)
    hero_id = Column(Integer, ForeignKey("players.id"))

    hero = relationship("Player", back_populates="heroes")
