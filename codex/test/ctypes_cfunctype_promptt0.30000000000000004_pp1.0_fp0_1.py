import ctypes
# Test ctypes.CFUNCTYPE.

from ctypes import *

def func(x):
    return x + 1

f = CFUNCTYPE(c_int, c_int)(func)

assert f(1) == 2
assert f(2) == 3

# Test ctypes.WINFUNCTYPE.

def func(x):
    return x + 1

