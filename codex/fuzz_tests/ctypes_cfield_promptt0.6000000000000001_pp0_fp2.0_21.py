import ctypes
# Test ctypes.CField.

import ctypes
import unittest
from test import support

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char),
                ("b", ctypes.c_char),
                ("c", ctypes.c_char)]

class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char),
                ("b", ctypes.c_char),
                ("c", ctypes.c_char)]

    def __init__(self, *args, **kw):
        super(Y, self).__init__(*args, **kw)
        self.a = b"a"
        self.b = b"b"
        self.c = b"c"

    def __eq__(self, other):
        return (super(Y, self).__eq__(other) and
                self.a == other.a and
                self.b == other.b and
                self.c == other.c)

class Z(Y):
    def __init__(self,
