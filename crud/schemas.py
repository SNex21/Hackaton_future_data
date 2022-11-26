from pydantic import BaseModel

class Img(BaseModel):
    api: str
    age: int
    male: str
    picType: str
    usrType: bool
    step:str

    class Config:
        orm_mode = True



class imageList(BaseModel):
    id: int
    age: int
    male: str
    img: str
    picType: str
    usrType: bool
    step: str

    class Config:
        orm_mode = True