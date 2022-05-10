import ctypes
# Test ctypes.CFUNCTYPE
#
# This test is for a bug in ctypes where the calling convention of a
# function pointer was not properly set.
#
# The bug was fixed in ctypes 0.9.9.2.
#
# This test is not run when using Python 2.3, because ctypes 0.9.9.2
# is not available for Python 2.3.

import sys
if sys.version_info[:2] < (2, 4):
    raise ImportError("test not supported in this python version")

from ctypes import *

# This is the function pointer type we want to use.
# It should be a stdcall function pointer.
CallBackFuncType = CFUNCTYPE(c_int, c_int, c_int)

# This is the function that will be called.
# It should be called with stdcall.
@WINFUNCTYPE(c_int, c_int, c_int)
def CallBackFunc(a, b):
    print "CallBackFunc", a, b
    return a + b

# This is the function that
