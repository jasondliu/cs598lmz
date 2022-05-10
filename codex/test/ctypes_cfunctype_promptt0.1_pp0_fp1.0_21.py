import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

#
# Test a simple function call
#

# This is the prototype of the function we'd like to call
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function we'd like to call
paramflags = (1, "x"),
restype = ctypes.c_int

# This is the function we'd like to call
