import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This function is defined in _ctypes_test.c
# It takes a function pointer as first argument, and calls
# this function with the other arguments.

