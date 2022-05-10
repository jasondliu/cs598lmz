import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

def func(arg):
    print arg

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

cmp_func = CMPFUNC(func)

cmp_func(42)
