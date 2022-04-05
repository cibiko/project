from sqlalchemy.orm import Session

from . import models, schemas



def register_player(db: Session, email: str = "abc", name: str = "abc"):
    return db.query(models.Player).offset(email).name(name)



def getting_hero_for_player(db: Session, player_name: str = 'abc' , hero_name: str = 'abc'):
    return db.query(models.Hero).offset(player_name).hero_name(hero_name).all()


def changing_the_hero_name(db: Session, name: str = "abc", limit: int = 50):
    return db.query(models.Hero).offset(name).limit(limit).all()



def read_heroes(db: Session, hero_id: int = 0 , limit: int = 100):
    return db.query(models.Hero).offset(hero_id).limit(limit).all()



def create_player_hero(db: Session, hero: schemas.HeroCreate, player_id: int,):
    return db.query(models.Player).offset(player_id).hero(hero)



