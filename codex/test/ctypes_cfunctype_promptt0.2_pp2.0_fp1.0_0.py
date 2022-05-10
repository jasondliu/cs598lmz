import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must take an integer argument and return an integer.

# The prototype of the function pointer is:
# int func(int)

FUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# The prototype of the function is:
# int test_callback(int (*func)(int), int arg)

