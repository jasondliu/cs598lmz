import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a callback

def func(x):
    return x * 2

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

lib.set_callback.argtypes = (CALLBACK,)
lib.set_callback.restype = None

lib.set_callback(CALLBACK(func))

if lib.call_callback(5) != 10:
    raise RuntimeError("callback failed")

# call a function with a callback, and pass a pointer to a function
# pointer

def func(x):
    return x * 2

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

lib.set_callback.argtypes = (CALLBACK,)
lib.set_callback.restype = None

lib.set_callback(CALLBACK(func))

if lib.call_callback(5
