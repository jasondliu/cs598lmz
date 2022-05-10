import ctypes
# Test ctypes.CField
#
# This test is based on the _ctypes test_cfield.py test, but modified to
# test that PEP 3118 buffer interface access to fields works correctly.
#
# This test depends on the _ctypes test_cfield.py test working correctly.

import unittest
from test import support

import _ctypes_test

class CFieldTestCase(unittest.TestCase):
    def test_cfield(self):
        obj = _ctypes_test.get_obj()
        self.assertEqual(obj.c, ord("X"))
        self.assertEqual(obj.c_string, "Hello")
        self.assertEqual(obj.c_wchar, "X")
        self.assertEqual(obj.c_wstring, "Hello")
        self.assertEqual(obj.c_short, -123)
        self.assertEqual(obj.c_int, -123)
        self.assertEqual(obj.c_long, -123)
        self.assertEqual(obj.c_longlong, -
