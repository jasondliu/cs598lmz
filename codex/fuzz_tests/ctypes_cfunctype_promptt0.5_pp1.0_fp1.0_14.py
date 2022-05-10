import ctypes
# Test ctypes.CFUNCTYPE

from ctypes import *

def func(x):
    return x * 2

prototype = CFUNCTYPE(c_int, c_int)

cfunc = prototype(func)

print cfunc(2)

if cfunc(2) != 4:
    raise Exception("test failed")
