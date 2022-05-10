import ctypes
# Test ctypes.CFUNCTYPE

import ctypes
import _ctypes_test

def func(*args):
    print(args)

CALLBACK = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)

callback = CALLBACK(func)

_ctypes_test.set_callback(callback)
_ctypes_test.call_callback(1, 2)

# Test ctypes.WINFUNCTYPE

import ctypes
import _ctypes_test

def func(*args):
    print(args)

CALLBACK = ctypes.WINFUNCTYPE(None, ctypes.c_int, ctypes.c_int)

callback = CALLBACK(func)

_ctypes_test.set_callback(callback)
_ctypes_test.call_callback(1, 2)

# Test ctypes.PYFUNCTYPE

import ctypes
import _ctypes_test

def func(*args):
    print(args)

CALLBACK = ctypes.PYFUNCTYPE(None
