import ctypes
# Test ctypes.CField.
#
# This test is a bit sketchy, as it relies on the name of the
# structure, which is platform-dependent.

import unittest
from test import support

class CFieldTest(unittest.TestCase):

    def test_basic(self):
        # Test basic functionality
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.a.size, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(X.b.offset, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(X.b.size, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(X.b.offset, X.a.size)

    def test_bitfields(self):
        # Test bitfields
        class X(ctypes.Structure):

