import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

def func(a, b):
    return a+b

f = ctypes.CFUNCTYPE(ctypes.c_int)(func)

