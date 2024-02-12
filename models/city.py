#!/usr/bin/python3
"""Define class City"""
from models.base_model import BaseModel


class City(BaseModel):
    """Defines city

    Attributes:
        state_id(str): states id
        name(str): name of city
    """
    state_id = ''
    name = ''
