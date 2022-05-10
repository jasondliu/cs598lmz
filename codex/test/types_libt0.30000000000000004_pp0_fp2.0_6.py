import types
types.MethodType(lambda self: None, None, object)

# TypeError: unbound method __init__() must be called with object instance as first argument (got nothing instead)

# __init__() method of the class is implicitly called when an instance of the class is created.

# The first argument of the __init__() method is always self.

# It is used to refer to the attributes and methods of the class in python.

# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)

