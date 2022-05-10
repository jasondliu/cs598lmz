import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

#
# First test a function with a simple result type
#

# int func(int)
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

