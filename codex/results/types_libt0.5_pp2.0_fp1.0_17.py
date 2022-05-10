import types
types.ModuleType.__repr__ = lambda self: self.__name__
from . import *
del types.ModuleType.__repr__
