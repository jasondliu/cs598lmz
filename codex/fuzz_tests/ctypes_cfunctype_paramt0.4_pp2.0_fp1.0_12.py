import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def make_function(name, nargs, func):
    """
    Make a function callable from C.
    """
    if nargs == 1:
        ftype = FUNTYPE
    else:
        raise NotImplementedError("nargs=%d" % nargs)
    cfunc = ftype(func)
    cfunc.__name__ = name
    return cfunc

def make_ufunc(name, nargs, func):
    """
    Make a function callable from C.
    """
    if nargs == 1:
        ftype = FUNTYPE
    else:
        raise NotImplementedError("nargs=%d" % nargs)
    cfunc = ftype(func)
    cfunc.__name__ = name
    return cfunc

def test_ufunc_1():
    def f(x):
        return x * 2
    cfunc = make_ufunc('test_ufunc_1', 1, f)
    assert cfunc(1.5)
