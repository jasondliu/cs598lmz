import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a c_int argument, and a c_int result
restype = ctypes.c_int
argtypes = (ctypes.c_int,)

# the prototype is c_int func(c_int)
prototype = ctypes.CFUNCTYPE(restype, *argtypes)

