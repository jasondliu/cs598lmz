import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer argument
# the function pointer argument is a Python callable

def func(x):
    return x * 2

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

lib.test_callback.argtypes = (CALLBACK,)
lib.test_callback.restype = ctypes.c_int

res = lib.test_callback(CALLBACK(func))
if res != 6:
    raise RuntimeError("callback failed")

# call a function with a function pointer argument
# the function pointer argument is a ctypes callback instance

def func(x):
    return x * 2

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

lib.test_callback.argtypes = (CALLBACK,)
lib.test_callback.restype = ctypes.c_int

cb =
