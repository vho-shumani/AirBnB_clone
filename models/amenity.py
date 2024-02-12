#!/usr/bin/python3
"""Define class Amenity and inherets from BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents the amenity

    Attributes:
        name(str): name of amenity
    """
    name = ''
