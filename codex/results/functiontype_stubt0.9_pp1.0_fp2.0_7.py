from types import FunctionType
a = (x for x in [1])
b = range(3).__iter__()
c = range(3)
print (isinstance(a, __internal__.Generator))
print (isinstance(b, __internal__.Iterator))
print (isinstance(c, __internal__.Iterable))

__DBG__ = """
import types
from types import FunctionType
a = (x for x in [1])
b = range(3).__iter__()
c = range(3)
print (isinstance(a, types.GeneratorType))
print (isinstance(b, types.GeneratorType))
print (isinstance(c, types.Iterable))

"""
__REF__[25] = """
import types
from types import FunctionType
Help on module types:

NAME
    types - Useful functions that used to be module global builtins.

FILE
    (built-in)

FUNCTIONS
    __import__(name, globals={'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_import
