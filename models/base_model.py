#!/usr/bin/python3
import uuid
from datetime import datetime

"""
Basemodel that defines attributes and
methods for the base class
"""


class BaseModel:
    """
    function instantiation of
    attributes
    """

    def __init__(self, id, created_at, updated_at):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    """
    function to print out 
    string value of attributes
    """

    def __str__(self):
        x = "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
        return x
    """
    updating the current
    instance of upadated_at
    using the save() function
    """

    def save(self):
        self.updated_at = datetime.now()
    """
    setting instance that
    will return
    """

    def to_dict(self):
        objdict = self.__dict__.copy
        objdict["__class__"] = self.__class__.__name__
        objdict["created_at"] = self.datetime.isoformat()
        objdict["updated_at"] = self.datetime.isoformat()
        return objdict
