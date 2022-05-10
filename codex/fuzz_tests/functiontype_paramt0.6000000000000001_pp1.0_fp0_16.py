from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

list(FunctionType(lambda x: None, {}).__code__.co_varnames)

list(FunctionType(lambda x, *y: None, {}).__code__.co_varnames)

list(FunctionType(lambda x, y, **z: None, {}).__code__.co_varnames)

list(FunctionType(lambda x, y, *z, **w: None, {}).__code__.co_varnames)

list(FunctionType(lambda x, y, *z, a, b=1, c=2, **w: None, {}).__code__.co_varnames)

# FunctionType.__code__ is read-only
import sys
def f(): pass

try:
    f.__code__ = None
except TypeError:
    print("TypeError")

try:
    f.__code__ = sys.getrefcount
except TypeError:
    print("TypeError")
