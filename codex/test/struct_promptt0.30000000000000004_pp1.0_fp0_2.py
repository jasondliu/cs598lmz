import _struct
# Test _struct.Struct

# This tests the basic functionality of _struct.Struct.

import _struct
import sys
import unittest
from test import support

class StructTest(unittest.TestCase):
    def test_format(self):
        # Test format string validation
        self.assertRaises(TypeError, _struct.Struct, "")
        self.assertRaises(TypeError, _struct.Struct, "abc")
        self.assertRaises(TypeError, _struct.Struct, "abcdef")
        self.assertRaises(TypeError, _struct.Struct, "abcdefgh")
        self.assertRaises(TypeError, _struct.Struct, "abcdefghi")
        self.assertRaises(TypeError, _struct.Struct, "abcdefghij")
        self.assertRaises(TypeError, _struct.Struct, "abcdefghijk")
        self.assertRaises(TypeError, _struct.Struct, "abcdefghijkl")
        self.assertRaises(TypeError, _struct.Struct, "abcdefghijklm")
