import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def make_func(name, argtype, restype, func):
    """
    return a ctypes function
    """
    return FUNTYPE((name, ctypes.CDLL(None)), (argtype, restype))

def make_func_np(name, argtype, restype, func):
    """
    return a numpy ufunc
    """
    cfunc = make_func(name, argtype, restype, func)
    return np.frompyfunc(cfunc, 1, 1)

def make_func_np_var(name, argtype, restype, func):
    """
    return a numpy ufunc
    """
    cfunc = make_func(name, argtype, restype, func)
    return np.vectorize(cfunc)

def make_func_np_var2(name, argtype, restype, func):
    """
    return a numpy ufunc
    """
    cfunc = make_func(name, argtype, restype, func)
