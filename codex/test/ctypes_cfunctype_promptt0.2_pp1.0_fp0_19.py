import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# prototype a function
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# create a function
restype = ctypes.c_int
argtypes = (ctypes.c_int,)

def func(arg):
    return arg * 2

cfunc = prototype(func)

# call the function
assert cfunc(5) == 10

# call the function through a pointer
