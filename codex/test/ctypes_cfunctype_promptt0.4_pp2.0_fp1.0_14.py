import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This function is called with an integer argument, and returns the
# square of this number. 

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# Callback functions must be registered using a Python
# function, with a C prototype.

# This function takes a function pointer as argument, and calls
# the function with an integer argument.

