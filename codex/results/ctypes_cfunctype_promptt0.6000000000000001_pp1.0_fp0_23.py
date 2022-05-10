import ctypes
# Test ctypes.CFUNCTYPE
from ctypes import *
import _ctypes_test

def func(x, y):
    return x+y

CALLBACK = CFUNCTYPE(c_int, c_int, c_int)
cb = CALLBACK(func)

if cb(1, 2) != 3:
    raise RuntimeError("CFUNCTYPE test failed")

# try some other argument types as well
CALLBACK = CFUNCTYPE(c_int, c_int, POINTER(c_int))
cb = CALLBACK(func)

if cb(1, byref(c_int(2))) != 3:
    raise RuntimeError("CFUNCTYPE test failed")

CALLBACK = CFUNCTYPE(c_int, POINTER(c_int), c_int)
cb = CALLBACK(func)

if cb(byref(c_int(1)), 2) != 3:
    raise RuntimeError("CFUNCTYPE test failed")

CALLBACK = CFUNCTYPE(c_int, POINTER(c_
