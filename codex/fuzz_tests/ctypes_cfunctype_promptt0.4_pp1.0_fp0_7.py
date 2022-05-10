import ctypes
# Test ctypes.CFUNCTYPE

from ctypes import *

def func(x, y):
    return x + y

FuncType = CFUNCTYPE(c_int, c_int, c_int)

f = FuncType(func)

print f(1, 2)

# This is the same:
f = CFUNCTYPE(c_int, c_int, c_int)(func)

print f(1, 2)

# This is the same:
f = CFUNCTYPE(c_int, c_int, c_int)

print f(1, 2)

# This is the same:
f = CFUNCTYPE(c_int, c_int, c_int)(lambda x, y: x + y)

print f(1, 2)

# This is the same:
f = CFUNCTYPE(c_int, c_int, c_int)(lambda x, y: x + y, None)

print f(1, 2)

# This is the same:
f = CFUNCTYPE
