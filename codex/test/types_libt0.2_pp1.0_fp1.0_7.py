import types
types.MethodType(lambda self: self.__class__.__name__, None, type)

# This is the class of the object you want to build.
class Foo(object):
    def __init__(self, name):
        self.name = name

# This is the factory function that builds Foo objects.
def foo_factory(name):
    return Foo(name)

# This is the factory function that builds Foo objects.
def foo_factory_with_type(name):
    return Foo(name), Foo.__name__

# This is the class of the object you want to build.
class Bar(object):
    def __init__(self, name):
        self.name = name

# This is the factory function that builds Bar objects.
def bar_factory(name):
    return Bar(name)

# This is the factory function that builds Bar objects.
def bar_factory_with_type(name):
    return Bar(name), Bar.__name__

# This is the class of the object you want to build.
