import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

def func(a, b):
    return a + b

CFunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

f = CFunc(func)

