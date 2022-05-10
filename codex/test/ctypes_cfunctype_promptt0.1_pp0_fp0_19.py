import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointed to must return an int, and take two ints
# as arguments.

# The prototype of the function is:
# int callit(int (*func)(int, int), int arg1, int arg2)

