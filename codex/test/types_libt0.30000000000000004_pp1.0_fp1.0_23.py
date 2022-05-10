import types
types.MethodType(lambda self, x: x, None)

# Test that the __new__ method of a metaclass is called with the correct
# arguments.
class Meta(type):
    def __new__(meta, name, bases, dict):
        assert meta is Meta
        assert name == "Foo"
        assert bases == (object,)
        assert dict == {"bar": True}
        return type.__new__(meta, name, bases, dict)

class Foo(object):
    __metaclass__ = Meta
    bar = True

# Test that the __init__ method of a metaclass is called with the correct
# arguments.
class Meta(type):
    def __init__(meta, name, bases, dict):
        assert meta is Foo
        assert name == "Foo"
        assert bases == (object,)
        assert dict == {"bar": True}

class Foo(object):
    __metaclass__ = Meta
    bar = True

# Test that the __prepare__ method of a metaclass is called with the correct
# arguments.
