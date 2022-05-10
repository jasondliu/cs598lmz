import types
types.ModuleType.__getattr__ = lambda self, key: lambda *args, **kwargs: self.__getattribute__(key)(*args, **kwargs)
