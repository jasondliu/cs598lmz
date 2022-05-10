import ctypes
# Test ctypes.CFUNCTYPE

def func(x):
    return x + 1

CFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

p = CFUNC(func)
