import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer argument

# prototype of the function we want to call
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# the function we want to call
def func(arg):
    print("func", arg)
    return arg + 42

# convert the Python function into a C function
cfunc = prototype(func)

# call the C function
