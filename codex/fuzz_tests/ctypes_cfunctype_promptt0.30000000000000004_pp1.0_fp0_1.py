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

f = WINFUNCTYPE(c_int, c_int)(func)

assert f(1) == 2
assert f(2) == 3

# Test ctypes.PYFUNCTYPE.

def func(x):
    return x + 1

f = PYFUNCTYPE(c_int, c_int)(func)

assert f(1) == 2
assert f(2) == 3

# Test ctypes.CFUNCTYPE with a function pointer.

def func(x):
    return x + 1

f = CFUNCTYPE(c_int, c_int)(func)

g = CFUNCTYPE(c_int, c_int)(f
