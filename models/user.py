#!/usr/bin/python3
"""Module defines the User class that inherets from the BaseModel class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Classe manage user objects

    Attribute:
    email(str)
    password(str)
    first_name(str)
    last_name(str)
    """

    email = ''
    password = ''
    first_name = ''
    last_name = ''
