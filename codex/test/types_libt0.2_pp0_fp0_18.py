import types
types.MethodType(lambda self: None, None, object)

# Test that the __new__ method of a metaclass is called with the correct
# arguments.
class Meta(type):
    def __new__(cls, name, bases, dct):
        return super(Meta, cls).__new__(cls, name, bases, dct)

class A(object):
    __metaclass__ = Meta

# Test that the __init__ method of a metaclass is called with the correct
# arguments.
class Meta(type):
    def __init__(cls, name, bases, dct):
        super(Meta, cls).__init__(name, bases, dct)

class A(object):
    __metaclass__ = Meta

# Test that the __call__ method of a metaclass is called with the correct
# arguments.
class Meta(type):
    def __call__(cls, *args, **kwargs):
        return super(Meta, cls).__call__(*args, **kwargs)

