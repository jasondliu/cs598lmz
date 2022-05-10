import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a callback

def func(x):
    return x * 2

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

res = lib.call_function(CALLBACK(func), 3)
if res != 6:
    raise RuntimeError("wrong result")

# call a function with a callback, and pass a pointer to the callback

def func(x):
    return x * 2

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

res = lib.call_function_ptr(CALLBACK(func), 3)
if res != 6:
    raise RuntimeError("wrong result")

# call a function with a callback, and pass a pointer to the callback
# and a pointer to the data

def func(x, y):
    return x * y

CALLBACK = ctypes.CF
