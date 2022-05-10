import ctypes
# Test ctypes.CFUNCTYPE

from ctypes import *

def func(x, y):
    return x + y

FuncType = CFUNCTYPE(c_int, c_int, c_int)

f = FuncType(func)

