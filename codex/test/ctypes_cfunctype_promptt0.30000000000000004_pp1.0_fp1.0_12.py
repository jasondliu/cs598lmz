import ctypes
# Test ctypes.CFUNCTYPE

from ctypes import *

def func(x, y):
    return x + y

# CFUNCTYPE(restype, *argtypes)
Add = CFUNCTYPE(c_int, c_int, c_int)(func)
