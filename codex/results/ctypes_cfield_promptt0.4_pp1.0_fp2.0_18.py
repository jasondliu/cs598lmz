import ctypes
# Test ctypes.CField

# This test is just to ensure that the CField object is created
# properly.  It is not a test of the functionality of the object.

import ctypes
from ctypes import *

class X(Structure):
    _fields_ = [("a", c_int),
                ("b", c_int)]

x = X()
assert x.a == x.b == 0

assert X.a.offset == 0
assert X.b.offset == sizeof(c_int)

assert X.a.size == sizeof(c_int)
assert X.b.size == sizeof(c_int)

assert X.a.type is c_int
assert X.b.type is c_int

assert X.a.index == 0
assert X.b.index == 1

assert X.a.pack == 1
assert X.b.pack == 1

assert X.a.bitsize is None
assert X.b.bitsize is None

assert X.a.bitoffset is None
assert X.b.bitoffset is None

assert X.a.flags
