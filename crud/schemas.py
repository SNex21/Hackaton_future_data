from pydantic import BaseModel

class Img(BaseModel):
    api: str
    age: int
    male: str
    category_id: int
    class Config:
        orm_mode = True


class Category(BaseModel):
    api: str
    name: str


class imageList(BaseModel):
    id: int
    age: int
    male: str
    img: str
    category_id: int

    class Config:
        orm_mode = True