from typing import List

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.post("/players/{email}/{name}/", response_model=schemas.Player)
def register_player(db: Session= Depends(get_db), email: str = "abc",name: str = "abc"):
   db_player=crud.register_player(db=db, email=email, name=name)
   return db_player


@app.put("/players/{hero_name}", response_model=schemas.Hero)
def changing_the_hero_name(db: Session = Depends(get_db),name="abc", limit=50):
    db_hero = crud.changing_the_hero_name(db=db, name=name, limit=limit)
    return db_hero


@app.get("/players/{player_name}/{hero_name}/", response_model=schemas.Hero)
def getting_hero_for_player(db: Session = Depends(get_db),player_name: str ="abc", hero_name: str = 'abc'):
    db_hero = crud.getting_hero_for_player(db=db, player_name=player_name, hero_name=hero_name)
    return db_hero


@app.post("/players/{player_id}/heroes/", response_model=schemas.Hero)
def create_hero_for_player(player_id: int, hero: schemas.HeroCreate, db: Session = Depends(get_db)):
    return crud.create_player_hero(db=db, hero=hero, player_id=player_id)


@app.get("/heroes/{hero_id}/", response_model=List[schemas.Hero])
def read_heroes(hero_id: int = 0, limit: int = 100,db: Session = Depends(get_db)):
    heroes = crud.read_heroes(db=db, hero_id=hero_id, limit=limit)
    return heroes
