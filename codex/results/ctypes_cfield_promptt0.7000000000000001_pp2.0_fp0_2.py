import ctypes
# Test ctypes.CField
#

import _ctypes_test

lib = ctypes.CDLL(None)

class X(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.c_int),
        ("b", ctypes.c_int),
    ]

    def __init__(self):
        self.a = 3
        self.b = 4

class Y(ctypes.Structure):
    _fields_ = [
        ("x", X),
        ("y", ctypes.c_char),
    ]

# the fields of X are duplicated in Y
# CFields are used to make this work
assert Y.x.a.offset == X.a.offset
assert Y.x.b.offset == X.b.offset

# Test that accessing the field a of the sub-structure X
# through the CField x.a and directly through Y.x.a
# yields the same result.
y = Y()
y.x.a = 99
assert y.x.a == 99
assert y.x.a == y.x
