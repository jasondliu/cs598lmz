import types
types.ModuleType.__repr__ = lambda self: self.__name__

from . import *

__all__ = [name for name in dir() if not name.startswith('_')]
