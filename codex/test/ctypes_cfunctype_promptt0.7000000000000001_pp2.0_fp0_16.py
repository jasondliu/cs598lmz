import ctypes
# Test ctypes.CFUNCTYPE
def func1(x):
    "Test function that returns its argument"
    return x

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
cmp_func = CMPFUNC(func1)

cmp_func.__name__ = 'cmp_func'

