import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_double, ctypes.POINTER(ctypes.c_double))

def wrapper(x, f, *args):
    x = array(x, dtype=float)
    f = array(f, dtype=float)
    _wrapper(x, f, *args)
    return x, f

def _wrapper(x, f, *args):
    f = f.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
    f_solve = FUNTYPE(f)
    _solver(f_solve, x, *args)
