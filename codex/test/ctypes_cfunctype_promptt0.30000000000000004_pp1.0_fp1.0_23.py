import ctypes
# Test ctypes.CFUNCTYPE

# This test is not complete, but it does test some of the more
# interesting aspects of ctypes.CFUNCTYPE.

from ctypes import *
import _ctypes_test

lib = CDLL(_ctypes_test.__file__)

# This function is called from C, and returns a pointer to a function
# pointer.

