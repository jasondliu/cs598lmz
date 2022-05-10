import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# a function pointer
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# a function pointer as function argument
restype = ctypes.c_int
argtypes = (prototype, ctypes.c_int)

