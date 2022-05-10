import ctypes
# Test ctypes.CField
#
# This tests that we can dynamically create CFieds, and that these
# CFieds really have the correct fields.
#
# We also check that the field order is correct.
#

import ctypes
from ctypes import *

class X(Structure):
    pass

X._fields_ = [("a", c_int),
              ("b", c_int),
              ("c", c_int)]

a = X()
a.a = 1
a.b = 2
a.c = 3

assert a._fields_[0][0] == "a"
assert a._fields_[0][1] == c_int
assert a._fields_[0][2] == 1

assert a._fields_[1][0] == "b"
assert a._fields_[1][1] == c_int
assert a._fields_[1][2] == 2

assert a._fields_[2][0] == "c"
assert a._fields_[2][1] == c_int
assert a._fields_[2][2] == 3
