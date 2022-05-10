import ctypes
# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
#
# This is the equivalent of:
#
#     int (*)(int)
#
# in C.
#
# The returned function pointer should be callable with an integer argument.
#
# The function pointer should be able to be passed to another C function.
#
# The function pointer should be able to be stored in a ctypes instance
# attribute.

import unittest
