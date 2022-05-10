import ctypes
# Test ctypes.CField
#
# This test is a bit different from the others, because it uses a
# different way to get the expected result.

import unittest
from test import support

class CFieldTestCase(unittest.TestCase):

    def test_field_offset(self):
        # Test ctypes.CField.offset
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int),
                        ("c", ctypes.c_int)]
        self.assertEqual(ctypes.sizeof(X), 3 * ctypes.sizeof(ctypes.c_int))
        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.b.offset, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(X.c.offset, 2 * ctypes.sizeof(ctypes.c_int))

    def test_field_size(self):
        # Test ctypes.CField.size
        class
