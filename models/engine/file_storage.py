#!/usr/bin/python3

import json
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """FileStorage class is a class responsible for
    serialization and deserealization of a json file """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns dictionary of objects"""
        return FileStorage.__objects
    
    def new(self, obj):
        """adds new object to the dictionary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ method adds a new object to the __objects dictionary"""
        objects_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objects_dict, f)
    
    def reload(self):
        """This method serializes the __objects dictionary to a JSON file specified by __file_path."""
        try:
            with open(FileStorage.__file_path) as f:
                objects_dict = json.load(f)
                for key, obj_dict in objects_dict.items():
                    class_name, _ = key.split('.')
                    self.__objects[key] = eval(class_name)(**obj_dict)
                    if class_name == "User":
                        self.__objects[key] = User(**obj_dict)
                    elif class_name == "State":
                        from models.state import State
                        self.__objects[key] = State(**obj_dict)
                    elif class_name == "City":
                        from models.city import City
                        self.__objects[key] = City(**obj_dict)
                    elif class_name == "Amenity":
                        from models.amenity import Amenity
                        self.__objects[key] = Amenity(**obj_dict)
                    elif class_name == "Place":
                        from models.place import Place
                        self.__objects[key] = Place(**obj_dict)
                    elif class_name == "Review":
                        from models.review import Review
                        self.__objects[key] = Review(**obj_dict)
        except FileNotFoundError:
            pass
    
    def all(self):
        """returns dictionary of objects"""
        return self.__objects
    
