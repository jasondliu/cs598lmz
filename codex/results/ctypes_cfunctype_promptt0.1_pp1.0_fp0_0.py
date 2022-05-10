import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer argument

# prototype of the function we want to call
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# the function we want to call
def func(value):
    return value + 1

# convert the Python function into a C function
cfunc = prototype(func)

# call the C function
res = lib.call_function(cfunc, 1)
if res != 2:
    raise RuntimeError("call_function returned %d, should be 2" % res)

# call a function with a function pointer argument
# and a user defined data pointer

# prototype of the function we want to call
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_void_p)

# the function we want to call
def func(value, data):
    return value + 1

# convert the
