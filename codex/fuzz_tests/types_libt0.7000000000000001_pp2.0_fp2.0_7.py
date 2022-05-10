import types
types.ModuleType = type
import importlib.machinery

class ModuleType(object):
    def __init__(self, name, loader=None):
        self.__name__ = name
        self.__loader__ = loader

    @property
    def __spec__(self):
        return importlib.machinery.ModuleSpec(
            self.__name__, self.__loader__)

    def __getattribute__(self, attr):
        try:
            return super(ModuleType, self).__getattribute__(attr)
        except AttributeError:
            if attr.startswith('__') and attr.endswith('__'):
                raise
            return importlib.import_module(self.__name__ + '.' + attr)
