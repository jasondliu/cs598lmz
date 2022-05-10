import ctypes
# Test ctypes.CField instance
#

import _ctypes_test

lib = _ctypes_test.dll

class X(ctypes.Structure):
    _fields_ = [
        ("myc", ctypes.c_char)
    ]

x = lib.getX()
print x.myc
