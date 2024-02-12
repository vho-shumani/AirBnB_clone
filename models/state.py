#!/usr/bin/python3
"""Module define State class inherets from BaseModel"""

from models.base_model import BaseModel


class State(BaseModel):
    """Represents the state

    Attributes:
        name: name of the state
    """
    name = ''
