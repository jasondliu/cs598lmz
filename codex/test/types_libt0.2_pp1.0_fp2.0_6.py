import types
types.MethodType(lambda self: None, None, object)

# Test that the __new__ method of a metaclass is called
class Meta(type):
    def __new__(cls, name, bases, dct):
        return super(Meta, cls).__new__(cls, name, bases, dct)

class A(object):
    __metaclass__ = Meta

# Test that the __new__ method of a metaclass is called
# even if the class has no __init__ method
class Meta(type):
    def __new__(cls, name, bases, dct):
        return super(Meta, cls).__new__(cls, name, bases, dct)

class A(object):
    __metaclass__ = Meta
    def __init__(self):
        pass

# Test that the __new__ method of a metaclass is called
# even if the class has no __init__ method and no __new__ method
