import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is the prototype of the function we want to call
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# Now we get the address of the function, and make a callable thing from it
restype = ctypes.c_int
argtypes = (ctypes.c_int,)
