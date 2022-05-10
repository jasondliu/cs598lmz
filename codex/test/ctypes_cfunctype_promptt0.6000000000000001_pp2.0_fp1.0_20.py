import ctypes
# Test ctypes.CFUNCTYPE()

def func(a, b):
    return a + b

cfunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)

