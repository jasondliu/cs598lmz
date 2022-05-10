import ctypes
# Test ctypes.CFUNCTYPE
#
# This test is a bit different from the others. It is not a test of
# the ctypes module, but of the CPython implementation.
#
# The test checks that the ctypes.CFUNCTYPE() function works
# correctly. The function is used to create callable objects from
# C function pointers.
#
# The test is not run if the 'ctypes' module is not compiled with
# support for CFUNCTYPE().

import sys

if not hasattr(ctypes, 'CFUNCTYPE'):
    raise ImportError("ctypes.CFUNCTYPE() is not available")

# The test is based on the following C code:
#
# #include <stdio.h>
#
# int add(int a, int b)
# {
#     return a+b;
# }
#
# int sub(int a, int b)
# {
#     return a-b;
# }
#
# int mul(int a, int b)
# {
#     return a*b;
# }
#
#
