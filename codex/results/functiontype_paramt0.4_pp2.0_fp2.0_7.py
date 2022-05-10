from types import FunctionType
list(FunctionType(lambda: None, globals()) for _ in range(10))

# function
def f():
    pass

list(FunctionType(f.__code__, f.__globals__, name=f.__name__, argdefs=f.__defaults__, closure=f.__closure__) for _ in range(10))

# class
class C:
    pass

list(C for _ in range(10))

# instance
class C:
    pass

list(C() for _ in range(10))

# module
import sys
list(sys for _ in range(10))

# generator
def g():
    yield 1

list(g() for _ in range(10))

# generator expression
list(x for x in range(10) for _ in range(10))

# dict
list({'a': 1} for _ in range(10))

# set
list({1} for _ in range(10))

# frozenset
list(frozenset({1}) for _ in range(10))

# tuple
