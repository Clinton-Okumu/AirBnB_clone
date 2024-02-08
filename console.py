#!/usr/bin/python3
"""Defines the HBnB console"""
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    
    def quit_program(self, arg):
        """quits the program"""
        return True
    
    def do_EOF(self, arg):
        """quit command to exit the program"""
        return True
    
    def empty_line(self):
        pass
    
    def create(self, arg):
        "Creates a new instance of Basemodel and saves it to JSON"""
        if not arg:
            print("** class name missing**")
            return
        try:
            instance_new = models.classes[arg]()
            instance_new.save()
            print(instance_new.id)
        except:
            print ("** class doesn't exist **")
    
    def show(self, arg):
        """prints string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in models.classes:
            print(" ** class doesn't exist ** ")
            return
        if len(args) < 2:
            print("** instance id is missing **")
            return
        key = args[0] + "." + args[1]
        if key in models.storage.all():
            print(models.storage.all()[key])
        else:
            print("** no instance found **")
        
    def destroy(self, arg):
        "deletes instance based on classname and id"
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key in models.storage.all():
            del models.storage.all()[key]
            models.storage.save()
        else:
            print("** no instance found **")
    
    def all(self, arg):
        'Prints string representation of all instances based or not on class name'
        args = arg.split()
        obj_list = []
        if not arg:
            for obj in models.storage.all().values():
                obj_list.append(str(obj))
            print(obj_list)
            return
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        for key, obj in models.storage.all().items():
            if key.split('.')[0] == args[0]:
                obj_list.append(str(obj))
        print(obj_list)
        
    def update(self, arg):
        'Updates an instance based on class name and id'
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in models.storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(models.storage.all()[key], args[2], args[3])
        models.storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
