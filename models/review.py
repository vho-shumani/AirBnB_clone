#!/usr/bin/python3
"""Module define class Review inherets from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Defines the revies

    Attributes:
        place_id(str): place id
        use(str): users id
        text(str): the review
    """
    place_id = ''
    user_id = ''
    text = ''
