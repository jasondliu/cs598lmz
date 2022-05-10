import ctypes
# Test ctypes.CField

try:
    ctypes.CField
except AttributeError:
    raise ImportError("requires ctypes")

import sys
if sys.platform == "win32":
    import _ctypes_test
else:
    import ctypes.test.test_cfield as _ctypes_test

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int)]

_ctypes_test.X = X

class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int)]

_ctypes_test.Y = Y

class Z(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int)]

_ctypes_test.
