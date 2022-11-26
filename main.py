from fastapi import FastAPI, File, UploadFile, Depends, HTTPException
from core.db import SessionLocal
from sqlalchemy.orm import Session
from PIL import Image
import shutil
import os
import crud.schemas as schemas
import crud.crud as crud
from core.settings import SECRET_KEY
from passlib.context import CryptContext
from typing import List


app = FastAPI()


# Сессия базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


hasher= CryptContext(schemes=['bcrypt'])


@app.post('/create_img')
def get_all_db(img_dep: schemas.Img = Depends(), file: UploadFile = File(...), db: Session = Depends(get_db),):
    if crud.get_api_by_value(db=db, value=img_dep.api) != None:
        img_dep = img_dep.dict()

        with open('media/'+file.filename, "wb") as image: # сохраняем картинки
            shutil.copyfileobj(file.file, image)
            img_path = str('media/' + file.filename)
            img = Image.open(img_path)
            fixed_width = 1600
            height_size = 1000
            new_image = img.resize((fixed_width, height_size)) # Обрезаем картинки
            new_image.save(img_path)
            image.close()

        crud.create_img(db=db, img_dep=img_dep, img_path=img_path)

        return {"message": "Succsesful!!!"}
    else:
        raise HTTPException(status_code=400, detail="error api key not found")


@app.post('/create_category')
def create_category(cat: schemas.Category, db: Session = Depends(get_db)):
    if crud.get_api_by_value(db=db, value=cat.api) != None:
        crud.create_category(db=db, category=cat)

        return {"message": "Succsesful!!!"}
    else:
        raise HTTPException(status_code=400, detail="error api key not found")


@app.post('/get_api_key')
def create_apikey(spec_key:str, db: Session = Depends(get_db)):
    if spec_key == SECRET_KEY :
        
        value = hasher.hash(crud.generate_random_string(50))
        crud.create_api_key(db=db, value=value)
        return {"api_key":value}
    else:
        raise HTTPException(status_code=400, detail="error api key not found")


@app.get('/get_all', response_model=List[schemas.imageList])
def get_all(db: Session = Depends(get_db)):
    return crud.get_all(db=db)
