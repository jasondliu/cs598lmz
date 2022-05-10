import types
types.ModuleType.__dict__.__setitem__('__getattr__', lambda self, name: self.__getattribute__(name))

import sys, traceback

class Module(types.ModuleType):
    def __init__(self, name):
        super(Module, self).__init__(name)
        self.__path__ = []
        self.__package__ = name
        self.__loader__ = self

    def __getattr__(self, name):
        if name in ('__file__', '__path__', '__package__', '__loader__'):
            return self.__dict__[name]
        else:
            raise ImportError("No module named %s" % name)

    def __setattr__(self, name, value):
        if name in ('__file__', '__path__', '__package__', '__loader__'):
            self.__dict__[name] = value
        else:
            raise AttributeError("attribute %s is read-only" % name)

