import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# a simple function

def func(arg):
    "A simple function"
    return arg + 1

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# call the function with a ctypes callback

res = lib.set_callback(CALLBACK(func))
if res != 42:
    raise RuntimeError("set_callback returned %d, should be 42" % res)

# call the function with a python callback

res = lib.set_callback(func)
if res != 42:
    raise RuntimeError("set_callback returned %d, should be 42" % res)

# call the function with a python callback and a tuple argument
res = lib.set_callback((func, (1,)))
if res != 42:
    raise RuntimeError("set_callback returned %d, should be 42" % res)

# call the function with a python callback and a dict argument
res =
