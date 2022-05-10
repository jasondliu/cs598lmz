import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

#
# The function prototype
#
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

#
# The function we want to call
#
restype = ctypes.c_int
argtypes = (ctypes.c_int, ctypes.c_int)

#
# The function we want to call
#
