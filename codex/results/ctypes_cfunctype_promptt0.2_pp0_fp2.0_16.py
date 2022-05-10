import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer argument

# prototype of the function we want to call
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# the function we want to call
def func(value):
    print("func called with", value)
    return value + 1

# the function we want to call
def func_with_exception(value):
    print("func called with", value)
    raise ValueError

# the function we want to call
def func_with_error(value):
    print("func called with", value)
    return -1

# the function we want to call
def func_with_error_and_exception(value):
    print("func called with", value)
    raise ValueError

# convert the Python function into a C function
cfunc = prototype(func)

# call the C function
res = lib.call_function(cfunc, 1)

