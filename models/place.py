#!/usr/bin/python3
"""Module define class Place"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Defines the Place

    Attributes:
        city_id(str) - the City id
        user_id(str) - the User id
        name(str) : name of place
        description(str)
        number_rooms(integer)
        number_bathrooms(integer)
        max_guest(integer)
        price_by_night(integer)
        latitude(float)
        longitude(float)
        amenity_ids(list of str)
    """
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
