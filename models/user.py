#!/usr/bin/python3
"""Module defines the User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Classe manage user objects"""

    email = ''
    password = ''
    first_name = ''
    last_name = ''
