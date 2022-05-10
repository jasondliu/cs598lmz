import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

#
# Test calling a function with a function pointer argument
#

# A function taking a function pointer argument
functype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# A function taking a function pointer argument
