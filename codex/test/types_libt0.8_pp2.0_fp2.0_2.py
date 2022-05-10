import types
types.ModuleType

class ModuleType(types.ModuleType):

    def __repr__(self):
        return '<module %s>' % self.__name__

ModuleType.__repr__ = lambda self: '<module %s>' % self.__name__

mod_type = ModuleType(__name__)
sys.modules[__name__] = mod_type

from mylib import *

def get_loaded_modules():
    pass

