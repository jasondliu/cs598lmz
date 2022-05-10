import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a callback argument

def func(x):
    return x * 2

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

lib.set_callback.argtypes = CALLBACK,
lib.set_callback.restype = None

lib.call_callback.argtypes = None,
lib.call_callback.restype = ctypes.c_int

lib.set_callback(CALLBACK(func))

if lib.call_callback() != 42:
    raise RuntimeError("callback failed")

# call a function with a callback argument, and pass None

lib.set_callback(None)

if lib.call_callback() != -1:
    raise RuntimeError("callback failed")

# call a function with a callback argument, and pass a callback
# function created by ctypes

def func(x):
    return x * 2

CALLBACK =
