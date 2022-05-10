import ctypes
# Test ctypes.CFUNCTYPE()

# NOTE: This test must be run with python.exe, not python_d.exe, as it
#       tests the actual function prototypes.

from ctypes import *
import _ctypes_test

NULL = c_void_p(0)

## Callback functions

CALLBACKFUNC = CFUNCTYPE(c_int, c_int, c_int)

def func(a, b):
    return a + b

callback = CALLBACKFUNC(func)

##

## Calling functions using the prototype

InvokeCallback = _ctypes_test.InvokeCallback

InvokeCallback.argtypes = (CALLBACKFUNC, c_int)
InvokeCallback.restype = c_int

if InvokeCallback(callback, 10) != 15:
    raise RuntimeError, "InvokeCallback"

##

## Calling functions using the prototype

InvokeCallback = _ctypes_test.InvokeCallback

InvokeCallback.argtypes = (CFUNCTYPE(c_int, c_int, c_int), c
