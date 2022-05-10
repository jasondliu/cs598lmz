import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double)

def register(name, func):
    if isinstance(func, FUNTYPE):
        func.__name__ = name
        _registry[name] = func
    else:
        raise TypeError("Invalid function type")

class FunctionRegistry(dict):
    def __getitem__(self, key):
        return dict.__getitem__(self, key.lower())

    def __setitem__(self, key, value):
        dict.__setitem__(self, key.lower(), value)


_registry = FunctionRegistry()
</code>

