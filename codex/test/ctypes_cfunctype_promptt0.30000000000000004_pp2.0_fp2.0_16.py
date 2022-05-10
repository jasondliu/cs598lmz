import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

libc = ctypes.CDLL(None)

def func(x):
    return x + 1

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

cmp_func = CMPFUNC(func)

