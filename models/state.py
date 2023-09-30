#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from os import getenv
from models import storage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete-orphan")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Getter attribute that returns the list of City instances with
            state_id equals to the current State.id"""
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
