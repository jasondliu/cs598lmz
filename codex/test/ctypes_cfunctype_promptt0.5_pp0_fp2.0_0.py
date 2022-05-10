import ctypes
# Test ctypes.CFUNCTYPE
def func(arg):
    return arg

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int))

cmp_func = CMPFUNC(func)
