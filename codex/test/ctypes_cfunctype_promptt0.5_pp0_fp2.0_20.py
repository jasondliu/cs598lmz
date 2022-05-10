import ctypes
# Test ctypes.CFUNCTYPE
from ctypes import *

def func(x):
    return x + 1

f = CFUNCTYPE(c_int, c_int)(func)
