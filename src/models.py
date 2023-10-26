import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)



class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    image_url = Column(String(250), nullable=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250), nullable=True)
    climate = Column(String(250), nullable=True)
    population = Column(Integer, nullable=True)
    terrain = Column(String(250), nullable=True)
    diameter = Column(Float, nullable=True)
    surface_meter = Column(Integer, nullable=True)
    orbital_period = Column(Integer, nullable=True)

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    image_url = Column(String(250), nullable=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250), nullable=True)
    gender = Column(String(250), nullable=True)
    height = Column(Integer, nullable=True)
    hair_color = Column(String(250), nullable=True)
    eye_color = Column(Float, nullable=True)
    birth_year = Column(Integer, nullable=True)

class Vehicle(Base):
    __tablename__ = 'vehicle'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    image_url = Column(String(250), nullable=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250), nullable=True)
    model = Column(String(250), nullable=True)
    manufacturer = Column(String(250), nullable=True)
    price = Column(Float, nullable=True)
   
class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=False)
    character = relationship(Character)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=False)
    planet = relationship(Planet)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'), nullable=False)
    vehicle = relationship(Vehicle)

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    content = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)
    created_at = Column(DateTime, nullable=False)
    modified_at = Column(DateTime, nullable=False)
    
class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    comment = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    post = relationship(Post)
    created_at = Column(DateTime, nullable=False)
    modified_at = Column(DateTime, nullable=False)

    # Example of foreing key link
    #person_id = Column(Integer, ForeignKey('person.id'))
    #person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
