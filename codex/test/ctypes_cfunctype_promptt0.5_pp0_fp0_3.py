import ctypes
# Test ctypes.CFUNCTYPE

def func(x):
    return x+1

cf = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(func)

