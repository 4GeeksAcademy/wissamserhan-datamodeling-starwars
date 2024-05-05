import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    image = Column(String(250), nullable=False)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250))
    planet_id = Column(Integer, ForeignKey('planets.id'))
    planet = relationship("Planets")

class Favorite_type(Base):
    __tablename__ = 'favorite_type'
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, primary_key=True)
    planet = relationship(Planets)
    Character_id = Column (Integer, ForeignKey('planets.id'))
    character = relationship(Characters)



class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    relation_id = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("Users")
    favorite_type_id = Column(Integer, ForeignKey('favorite_type.id'))
    favorite_type = relationship("Favorite_type")

# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///sqlalchemy_example.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)

# Generate the ER diagram
render_er(Base, 'diagram.png')

