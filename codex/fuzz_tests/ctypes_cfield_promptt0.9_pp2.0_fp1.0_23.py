import ctypes
# Test ctypes.CField.

import os, pickle, sys, traceback
import unittest
from test import test_support

try:
    unicode
except NameError:
    unicode = str

class TestCField(unittest.TestCase):
    def test_basic(self):
        # Test basic structure field access.
        class POINT(ctypes.Structure):
            _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]
        pt = POINT(10, 20)
        self.assertEqual(pt.x, 10)
        self.assertEqual(pt.y, 20)

        # This should fail with a TypeError
        self.assertRaises(TypeError, setattr, pt, 'x', "hello, world")

        pt.x = 5
        self.assertEqual(pt.x, 5)

    def test_byval(self):
        # Test _argument_
        class POINT(ctypes.Structure):
            _fields_ = [('x', ctypes.c_int), ('
