import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must have the same signature as the
# CFUNCTYPE function we pass.

# The prototype of the function is:
# int function(int(*)(int))

FUNCTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# The function takes a function pointer as argument.  The function
# pointer must have the same signature as the CFUNCTYPE function we
# pass.

# The prototype of the function is:
# int function(int(*)(int))

@FUNCTYPE
def func(n):
    "A Python function that takes an integer argument and returns an integer"
    return n * 10

lib.pass_func.argtypes = (FUNCTYPE,)
lib.pass_func.restype = ctypes.c_int

# The function returns the value passed to the function pointer
# multiplied
