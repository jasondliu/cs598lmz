import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must have the same signature as the
# CFUNCTYPE() object we pass.

prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# The following function takes a function pointer as first argument.
# The function must return an integer, and take an integer as argument.
# The integer argument is passed to the function pointer.

restype = ctypes.c_int
argtypes = (prototype, ctypes.c_int)

# The following function is called from Python.  It calls the
# function pointer, and returns the result.

def callit(func, arg):
    func.restype = restype
    func.argtypes = argtypes
    return func(arg)

# The following function is called from C.  It calls the
# function pointer, and returns the result.

