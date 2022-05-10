import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

def func(x, y):
    return x + y

CFunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

cfunc = CFunc(func)

