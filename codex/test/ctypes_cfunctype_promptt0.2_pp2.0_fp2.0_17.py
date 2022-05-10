import ctypes
# Test ctypes.CFUNCTYPE

from ctypes import *

def func(x):
    return x * 2

CALLBACK = CFUNCTYPE(c_int, c_int)

callback = CALLBACK(func)

