import ctypes
# Test ctypes.CField

# This is a test for a bug that was fixed in 2.5.1.
# The problem was that a CField instance was not
# initialized correctly.

import ctypes

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

x = X()
x.a = 1
x.b = 2

print x.a, x.b
