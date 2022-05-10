import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

def func(x):
    return x + 1

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(func)
