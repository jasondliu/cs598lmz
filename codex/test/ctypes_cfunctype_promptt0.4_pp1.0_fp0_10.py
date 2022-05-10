import ctypes
# Test ctypes.CFUNCTYPE.
# This tests the case where the function has no arguments.

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

prototype = ctypes.CFUNCTYPE(ctypes.c_int)
restype = ctypes.c_int

