import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function taking a function pointer as argument
# The function pointer takes a double and returns a double
# The function returns a function pointer

prototype = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
paramflags = (1, "func"),

