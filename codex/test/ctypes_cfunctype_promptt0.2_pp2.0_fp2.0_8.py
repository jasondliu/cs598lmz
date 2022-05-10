import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a pointer argument

# This is the prototype of the function we call
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int))

# This is the prototype of the function we call
restype = ctypes.c_int
argtypes = (ctypes.POINTER(ctypes.c_int),)

# This is the function we call
