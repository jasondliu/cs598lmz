from types import FunctionType
list(FunctionType(code, globals(), name='foo'))

# class
import types
class Foo:
    def __getitem__(self, key):
        return key

type(Foo.__getitem__) == types.MethodType
list(Foo())

# function
def foo(x):
    return x

type(foo.__call__) == types.MethodType
list(foo(1))

# generator
def foo():
    yield 1
    yield 2
    yield 3

list(foo())

# iterator
import collections
foo = collections.deque(range(3))
list(foo)

# custom
class Foo:
    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self):
        return iter(self.iterable)

list(Foo(range(3)))

# `__iter__` returns an `__iter__` method
class Foo:
    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self):
