import ctypes
# Test ctypes.CFUNCTYPE with a simple function

def func(x):
    return x

f = ctypes.CFUNCTYPE(ctypes.c_int)(func)

