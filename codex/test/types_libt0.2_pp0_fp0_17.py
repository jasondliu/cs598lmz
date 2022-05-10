import types
types.MethodType(lambda self, x: x, None, None)

# Test that the __new__ method of a metaclass is called with the correct
# arguments.
class Meta(type):
    def __new__(cls, name, bases, dct):
        assert cls is Meta
        assert name == 'Foo'
        assert bases == (object,)
        assert dct == {'bar': 42}
        return super(Meta, cls).__new__(cls, name, bases, dct)

class Foo(object):
    __metaclass__ = Meta
    bar = 42

# Test that the __init__ method of a metaclass is called with the correct
# arguments.
class Meta(type):
    def __init__(cls, name, bases, dct):
        assert cls.__name__ == 'Foo'
        assert cls.__bases__ == (object,)
