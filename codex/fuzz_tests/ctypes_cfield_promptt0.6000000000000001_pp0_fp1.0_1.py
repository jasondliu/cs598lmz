import ctypes
# Test ctypes.CField:
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]

#
# The following tests are taken from the ctypes tests,
# and are copied here to verify that the ctypes module
# still works after the patch.
#
import unittest
from test import test_support

class StructureTestCase(unittest.TestCase):
    def test_fields(self):
        self.assertEqual(X._fields_, [("a", ctypes.c_int), ("b", ctypes.c_int)])

        class Y(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int),
                        ("c", X)]
        self.assertEqual(Y._fields_, [("a", ctypes.c_int),
                                      ("b", ctypes.c_int),
                                      ("c", X)])

        class Z(ctypes.Structure):
            _fields_
