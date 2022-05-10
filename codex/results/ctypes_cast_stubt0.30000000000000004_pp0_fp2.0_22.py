import ctypes
ctypes.cast(0, ctypes.py_object)

# SOURCE: https://github.com/python/cpython/blob/3.7/Lib/ctypes/test/test_cast.py
# Test the cast() function.
import unittest
from test import support
from ctypes import *

class CastTestCase(unittest.TestCase):
    def test_cast(self):
        self.assertRaises(TypeError, cast, None, c_int)
        self.assertRaises(TypeError, cast, None, c_int)
        self.assertRaises(TypeError, cast, c_int, None)
        self.assertRaises(TypeError, cast, c_int, None)
        self.assertRaises(TypeError, cast, c_int, "abc")
        self.assertRaises(TypeError, cast, "abc", c_int)
        self.assertRaises(TypeError, cast, c_int, "abc")
        self.assertRaises(TypeError, cast, "abc", c_int)

        self.assertRaises
