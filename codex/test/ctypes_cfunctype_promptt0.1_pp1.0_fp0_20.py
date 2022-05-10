import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must have the same signature as the
# CFUNCTYPE function we pass.

prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# The following line is equivalent to:
#
#   restype = ctypes.c_int
#   argtypes = (ctypes.c_int,)
#   lib.myfunc.restype = restype
#   lib.myfunc.argtypes = argtypes
#
