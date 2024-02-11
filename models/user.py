#!/usr/bin/python3

"""Class user that inherits from BaseModel"""

from models.base_model import BaseModel

class User(BaseModel):
    """Class attributes:
    email: string - empty string
    password: string - empty string
    first_name: string - empty string
    last_name: string - empty string
    """
    def __init__(self, *args, **kwargs):
        """initializes user instance"""
        super().__init__(*args,**kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

