import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function pointer type
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# The following line is equivalent to
#   restype = ctypes.c_int
#   argtypes = (ctypes.c_int,)
#   lib.my_function.restype = restype
#   lib.my_function.argtypes = argtypes
#   my_function = lib.my_function
