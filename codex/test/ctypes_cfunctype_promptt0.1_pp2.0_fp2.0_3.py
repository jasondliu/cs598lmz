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

# The function must be passed as a pointer, so we must wrap it
# in a class.

