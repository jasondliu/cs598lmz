import ctypes
# Test ctypes.CField
#
# Run with python test_cfield.py
#
# No data file needed

from ctypes import *

class X(Structure):
    _fields_ = [("a", c_char),
                ("b", c_double),
                ("c", c_char)]

print X.a
