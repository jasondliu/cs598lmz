import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

#
# Test calling a function with a prototype
#

prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# The prototype is used to convert the arguments
