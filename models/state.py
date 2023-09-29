#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "State"
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state", cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            """Getter attribute that returns the list of City instances with
            state_id equals to the current State.id"""
            from models import storage
            city_list = []
            cities = storage.all("City")
            for city in cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
