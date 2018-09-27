import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class UserInfo(Base):
    __tablename__ = 'userinfo'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)

class UserAddress(Base):
    __tablename__ = 'useraddress'

    id = Column(Integer, primary_key= True)
    firstname = Column (String(80))
    lastname = Column (String(80))
    phone = Column (String(20))
    userInfo_id = Column(Integer, ForeignKey('userinfo.id'))
    userinfo = relationship(UserInfo)

engine = create_engine('sqlite:///father.db')

Base.metadata.create_all(engine)

