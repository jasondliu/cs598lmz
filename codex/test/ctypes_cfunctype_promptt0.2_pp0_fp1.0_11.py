import ctypes
# Test ctypes.CFUNCTYPE

def func(x):
    return x

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(func)
