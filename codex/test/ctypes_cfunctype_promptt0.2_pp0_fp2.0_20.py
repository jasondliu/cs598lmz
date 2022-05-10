import ctypes
# Test ctypes.CFUNCTYPE

# This test is for the CFUNCTYPE() function, which creates
# callable objects from C function pointers.

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# A simple function

