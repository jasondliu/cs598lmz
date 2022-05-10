import ctypes
# Test ctypes.CFUNCTYPE

from ctypes import *

# The following is a simple example of a C callback function.
# It is called from Python, and should return the sum of its
# two arguments.

CALLBACK = CFUNCTYPE(c_int, c_int, c_int)

