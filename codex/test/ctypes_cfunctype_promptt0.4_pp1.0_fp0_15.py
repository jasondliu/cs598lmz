import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# a function taking a function pointer as argument
# and returning a function pointer
restype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

