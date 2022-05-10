import types
types.ClassType

import sys

# The classes that we will be building up
class MyClass:
    pass

class MyDescriptor:
    def __get__(self, instance, owner):
        print("MyDescriptor.__get__(%s, %s)" % (instance, owner))

class MyMeta(type):
    def __new__(meta, name, bases, class_dict):
        print("MyMeta.__new__(%s, %s, %s)" % (meta, name, bases))
        return type.__new__(meta, name, bases, class_dict)

class MySubclass(MyClass):
    pass

# The class dictionary for MyClass
print("\nMyClass.__dict__ =", MyClass.__dict__)
print("MyClass.__class__ =", MyClass.__class__)
print("MyClass.__bases__ =", MyClass.__bases__)

