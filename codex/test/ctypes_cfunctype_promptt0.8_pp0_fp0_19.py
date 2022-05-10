import ctypes
# Test ctypes.CFUNCTYPE for functions that return void.

from ctypes import *

TestError = "TestError"

class X(Structure):
    pass
X._fields_ = [("a", c_int)]

p = pointer(X())

