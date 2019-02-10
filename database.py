
from model import *


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///users.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def add_user(name,age,email,skill_level,genre,instrument,notes):

  user_object = User(
    name=name,
    age=age,
    email=email,
    skill_level=skill_level,
    genre =genre, 
    instrument= instrument,
    notes=notes)
  print(user_object)
  session.add(user_object)
  session.commit()

def query_user_by_instrument(instrument):

  users = session.query(
      User).filter_by(
      instrument=instrument).all()
  print(users)
  return users

