from typing import List, Optional

from pydantic import BaseModel


class HeroBase(BaseModel):
    name: str
    email: Optional[str] = None


class HeroCreate(HeroBase):
    pass


class Hero(HeroBase):
    id: int
    hero_id: int
    name: str

    class Config:
        orm_mode = True


class PlayerBase(BaseModel):
    email: str



class Player(PlayerBase):
    email: str
    name: str
    id: int
    golds: int
    heroes: List[Hero] = []

    class Config:
        orm_mode = True
