import ctypes
# Test ctypes.CFUNCTYPE()
#
# The test case is a function with a pointer argument, which is
# passed a pointer to a structure.  The function returns the
# address of the structure.
#
# This test is not complete: it does not test whether the structure
# can be accessed.
#

import ctypes
from ctypes import *

class Point(Structure):
    _fields_ = [("x", c_int), ("y", c_int)]

def test_point():
    PFunc = ctypes.CFUNCTYPE(POINTER(Point), POINTER(Point))
    pfunc = PFunc(lambda p: p)
    p = Point(1, 2)
    p2 = pfunc(pointer(p))
    print(p2.contents)

