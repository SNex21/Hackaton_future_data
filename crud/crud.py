from sqlalchemy.orm import Session
from core import models
from . import schemas
import string
import random


def create_img(db: Session, img_dep: dict, img_path: str):
    db_img = models.Image(
        age=img_dep['age'],
        male=img_dep['male'],
        img = img_path,
        picType = img_dep['picType'],
        usrType = img_dep['usrType']

     )
    db.add(db_img)
    db.commit()
    db.refresh(db_img)
    return db_img



def create_api_key(db: Session, value: str, ):
    db_key = models.ApiToken(
        value = value
    )
    db.add(db_key)
    db.commit()
    db.refresh(db_key)
    return db_key


def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string

    
def get_api_by_value(db: Session, value: str):
    return db.query(models.ApiToken).filter(models.ApiToken.value == value).first()


def get_all(db: Session):
    return db.query(models.Image).all()


