import types
types.MethodType(lambda self: None, None, None)

# Test that the __new__ method of a metaclass is called with the correct
# arguments.
class Meta(type):
    def __new__(cls, name, bases, dct):
        return super(Meta, cls).__new__(cls, name, bases, dct)

class A(object):
    __metaclass__ = Meta

# Test that the __new__ method of a metaclass is called with the correct
# arguments when the class has a custom metaclass.
class Meta2(type):
    def __new__(cls, name, bases, dct):
        return super(Meta2, cls).__new__(cls, name, bases, dct)

class B(object):
    __metaclass__ = Meta2

# Test that the __new__ method of a metaclass is called with the correct
# arguments when the class has a custom metaclass and a custom __new__
# method.
class Meta3(type):
    def __new__(cl
