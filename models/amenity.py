#!/usr/bin/python3
"""Define class Amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Defines the amenity

    Attributes:
        name(str): name of amenity
    """
    name = ''
