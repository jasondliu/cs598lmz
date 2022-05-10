from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo'))

# __getitem__
class Foo:
    def __getitem__(self, key):
        return key

list(Foo())

# __iter__
class Foo:
    def __iter__(self):
        yield 1

list(Foo())

# __getattr__
class Foo:
    def __getattr__(self, name):
        return name

list(Foo())

# __getattribute__
class Foo:
    def __getattribute__(self, name):
        return name

list(Foo())

# __call__
class Foo:
    def __call__(self):
        yield 1

list(Foo())

# __new__
class Foo:
    def __new__(cls):
        return object.__new__(cls)

list(Foo())

# __init__
class Foo:
    def __init__(self):
        self.__iter__ = lambda: iter([1])

list(Foo())

#
