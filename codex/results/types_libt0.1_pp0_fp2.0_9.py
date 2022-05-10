import types
types.MethodType(lambda self, x: x, None, object)

# Test that the __new__ method of a metaclass is called with the correct
# arguments.
class Meta(type):
    def __new__(cls, name, bases, dct):
        return super(Meta, cls).__new__(cls, name, bases, dct)

class A(object):
    __metaclass__ = Meta

# Test that the __new__ method of a metaclass is called with the correct
# arguments.
class Meta(type):
    def __new__(cls, name, bases, dct):
        return super(Meta, cls).__new__(cls, name, bases, dct)

class A(object):
    __metaclass__ = Meta

# Test that the __new__ method of a metaclass is called with the correct
# arguments.
class Meta(type):
    def __new__(cls, name, bases, dct):
        return super(Meta, cls).__new__(cls, name, bases
