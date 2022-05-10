import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This function is declared in _ctypes_test.c as:
#   int func(int(*)(int))
