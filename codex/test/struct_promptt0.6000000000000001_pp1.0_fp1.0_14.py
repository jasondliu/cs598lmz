import _struct
# Test _struct.Struct class

import sys
import unittest
from test import support

import _struct

class StructTest(unittest.TestCase):
    def test_format(self):
        # test struct format
        self.assertRaises(TypeError, _struct.Struct, "I I")
        self.assertRaises(TypeError, _struct.Struct, "I 10s")
        self.assertRaises(TypeError, _struct.Struct, "I I I")
        self.assertRaises(TypeError, _struct.Struct, "c")
        self.assertRaises(TypeError, _struct.Struct, "c c")
        self.assertRaises(TypeError, _struct.Struct, "10c")
        self.assertRaises(TypeError, _struct.Struct, "x")
        self.assertRaises(TypeError, _struct.Struct, "")
        self.assertRaises(TypeError, _struct.Struct, "P")

