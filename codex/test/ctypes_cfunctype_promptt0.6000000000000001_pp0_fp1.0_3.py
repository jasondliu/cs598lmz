import ctypes
# Test ctypes.CFUNCTYPE

def func(x):
    return x+1

f = ctypes.CFUNCTYPE(ctypes.c_int)(func)

