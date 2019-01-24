from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :
class User(Base):
	__tablename__="users"
	user_id=Column(Integer,primary_key=True)
	name=Column(String)
	age=Column(String)
	email = Column(String)
	skill_level= Column(String)
	genre= Column(String)
	instrument=Column(String)
