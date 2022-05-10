import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This function takes a function pointer as argument
# and calls it.

# The prototype of the called function is:
# int func(int)

CALLFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# The prototype of the calling function is:
# int call_func(int (*func)(int), int arg)

