import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

class _C_FUNC(object):
    def __init__(self, func, argtypes):
        self.func = func
        self.argtypes = argtypes
    def __call__(self, *args):
        return self.func(*args)

class _C_FUNC_PTR(object):
    def __init__(self, func):
        self.func = func
    def __call__(self, *args):
        return self.func(*args)

def c_func(func, argtypes):
    return _C_FUNC(func, argtypes)

def c_func_ptr(func):
    return _C_FUNC_PTR(func)

def c_int(value):
    return ctypes.c_int(value)

def c_uint(value):
    return ctypes.c_uint(value)

def c_long(value):
    return ctypes.c_long(value)

def c_ulong(value):
    return ctypes.c_ulong(value)

