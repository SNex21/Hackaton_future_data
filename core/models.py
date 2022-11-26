from  core.db import Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship

class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, unique=True, primary_key=True, index=True)
    age = Column(Integer)
    male = Column(String(100))
    img = Column(String(4000), unique=True)
    picType = Column(String(255))
    usrType = Column(Boolean)


class ApiToken(Base):
    __tablename__='api_key'
    id = Column(Integer, primary_key=True, unique=True)
    value = Column(String(100), unique=True)
    




    

