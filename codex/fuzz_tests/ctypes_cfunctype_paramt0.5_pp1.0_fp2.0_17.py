import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def make_callable(func, argtypes=[ctypes.c_double], restype=ctypes.c_double):
    cfunc = FUNTYPE(func)
    cfunc.argtypes = argtypes
    cfunc.restype = restype
    return cfunc

def cfunc_factory(func, argtypes=[ctypes.c_double], restype=ctypes.c_double):
    cfunc = make_callable(func, argtypes, restype)
    def f(*args):
        return cfunc(*args)
    return f

def cfunc_factory2(func, argtypes=[ctypes.c_double], restype=ctypes.c_double):
    cfunc = make_callable(func, argtypes, restype)
    def f(x):
        return cfunc(x)
    return f

def cfunc_factory3(func, argtypes=[ctypes.c_double], restype=ctypes.c_double):
    cfunc = make_
