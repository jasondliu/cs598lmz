import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_int)

def register_func(func, index):
    """
    Register func as a function of one variable.
    index is the index of the variable.
    """
    cfunc = FUNTYPE(func)
    name = func.__name__
    functools.update_wrapper(cfunc, func)
    cfunc.__name__ = name
    cfunc.index = index
    cfunc.__doc__ = "A function of variable %d" % index
    globals()[name] = cfunc

if __name__ == "__main__":
    import doctest
    doctest.testmod()
