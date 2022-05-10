import ctypes
# Test ctypes.CField

# This tests the CField object.  It is a subclass of Field, and is
# used to define fields of a Structure which are pointers to other
# structures.  It also defines a _type_ attribute which is used to
# create the pointer type.

import unittest
from test import test_support

class CFieldTestCase(unittest.TestCase):
    def test_CField(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        class Y(ctypes.Structure):
            _fields_ = [("x", ctypes.POINTER(X))]

        self.assertEqual(Y._fields_[0][1]._type_, X)
        self.assertEqual(Y._fields_[0][1]._type_.__name__, "X")

        y = Y()
        x = X()
        x.a = 42
        y.x = ctypes.pointer(x)
        self.assertEqual(y.x.contents.a, 42)


