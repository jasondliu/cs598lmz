import types
types.ModuleType.__setattr__ = types.ModuleType.__setattr__

class MyModule(types.ModuleType):
    def __init__(self, name, doc=None):
        super(MyModule, self).__init__(name, doc)
        self.__dict__['__name__'] = name
        self.__dict__['__doc__'] = doc
        self.__dict__['__path__'] = []
        self.__dict__['__file__'] = ''
        self.__dict__['__package__'] = ''
        self.__dict__['__loader__'] = None
        self.__dict__['__spec__'] = None
        self.__dict__['__cached__'] = None

    def __setattr__(self, name, value):
        if name in ('__name__', '__doc__', '__path__', '__file__', '__package__', '__loader__', '__spec__', '__cached__'):
            self.__dict__[name] = value
        else:
            super(My
