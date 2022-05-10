import types
types.ModuleType.__subclasses__ = nolambda

#print 'dummy subclasses end'

### Hook for standard library modules

class DummyModule(types.ModuleType):
    def __init__(self, name, doc=None):
        types.ModuleType.__init__(self, name)
        self.__doc__ = doc

class DummyClass(object):
    def __init__(self, name, bases, dct):
        for k, v in dct.items():
            if isinstance(v, types.FunctionType):
                v = FunctionType(v.func_code, v.func_globals,
                                 name = '%s.%s' % (name, k),
                                 argdefs = v.func_defaults,
                                 closure = v.func_closure)
            setattr(self, k, v)

class DummyException(Exception):
    def __init__(self, name, bases, dct):
        self.__name__ = name
        for k, v in dct.items():
           
