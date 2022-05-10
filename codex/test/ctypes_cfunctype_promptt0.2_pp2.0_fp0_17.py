import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is the prototype of the function we want to call:
# int printf(const char *format, ...);

# The argtypes and restype attributes tell ctypes what the function
# prototype looks like.

