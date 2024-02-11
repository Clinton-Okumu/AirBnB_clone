#!/usr/bin/python3

import cmd
from models.engine.file_storage import storage
from models.user import User

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB console"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def help_EOF(self):
        print("EOF command to exit the program")

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        arg_list = arg.split()
        try:
            if arg_list[0] == "User":
                new_instance = User()
            else:
                new_instance = eval(arg_list[0])()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return
        arg_list = arg.split()
        try:
            if arg_list[0] not in storage.classes():
                print("** class doesn't exist **")
                return
            if len(arg_list) < 2:
                print("** instance id missing **")
                return
            key = "{}.{}".format(arg_list[0], arg_list[1])
            print(storage.all()[key])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        arg_list = arg.split()
        try:
            if arg_list[0] not in storage.classes():
                print("** class doesn't exist **")
                return
            if len(arg_list) < 2:
                print("** instance id missing **")
                return
            key = "{}.{}".format(arg_list[0], arg_list[1])
            del storage.all()[key]
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if not arg:
            print([str(value) for value in storage.all().values()])
            return
        arg_list = arg.split()
        try:
            if arg_list[0] not in storage.classes():
                print("** class doesn't exist **")
                return
            print([str(value) for key, value in storage.all().items()
                   if arg_list[0] in key])
        except KeyError:
            print("** no instance found **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        arg_list = arg.split()
        try:
            if arg_list[0] not in storage.classes():
                print("** class doesn't exist **")
                return
            if len(arg_list) < 2:
                print("** instance id missing **")
                return
            key = "{}.{}".format(arg_list[0], arg_list[1])
            if key not in storage.all():
                print("** no instance found **")
                return
            if len(arg_list) < 3:
                print("** attribute name missing **")
                return
            if len(arg_list) < 4:
                print("** value missing **")
                return
            setattr(storage.all()[key], arg_list[2], arg_list[3])
            storage.save()
        except KeyError:
            print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
