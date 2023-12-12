#!/usr/bin/python
""" hold a class called Amenity"""
    from models.base_model import BaseModel


    class Amenity(BaseModel):
        """Representation of Amenity"""
        name = ""

        def __int__(self, *args, **kwargs):
            """initialization of Amenity"""
            super().__int__(*args, **kwargs)
