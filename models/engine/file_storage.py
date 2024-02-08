#!/usr/bin/python3

import json


class FileStorage:
    """FileStorage class is a class responsible for
    serialization and deserealization of a json file """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns dictionary of objects"""
        return self.__objects
    
    def new(self, obj):
        """adds new object to the dictionary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ method adds a new object to the __objects dictionary"""
        objects_dict = {key: obj.to_dict() for key in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(objects_dict, f)
    
    def reload(self):
        """This method serializes the __objects dictionary to a JSON file specified by __file_path."""
        try:
            with open(self.__file_path, 'r') as f:
                objects_dict = json.load(f)
                for key, obj_dict in objects_dict.items():
                    class_name, obj_id = key.split(',')
                    self.__objects[key] = eval(class_name)(**obj_dict)
        except FileNotFoundError:
            pass
    
    def all(self):
        """returns dictionary of objects"""
        return self.__objects