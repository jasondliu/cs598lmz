import ctypes
# Test ctypes.CFUNCTYPE with no args

from ctypes import *
import _ctypes_test

libc = CDLL(_ctypes_test.__file__)

# First create a prototype
CMPFUNC = CFUNCTYPE(c_int, c_int, c_int)

# Next, an array type
# cmp_func is a user data item in the call back function
# we have to pass a pointer to the function, not just the function
CMPARRTYPE = c_int * 2
