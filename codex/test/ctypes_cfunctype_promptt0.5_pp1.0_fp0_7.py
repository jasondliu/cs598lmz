import ctypes
# Test ctypes.CFUNCTYPE

# Test a simple function pointer

import ctypes

def func(a, b):
    return a * b

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

f = CMPFUNC(func)
