import _struct
# Test _struct.Struct

import sys
import unittest
import struct

from test import support

class StructTestCase(unittest.TestCase):
    def test_format_string_validation(self):
        self.assertRaises(ValueError, _struct.Struct, "I I")
        self.assertRaises(ValueError, _struct.Struct, "I I I")
        self.assertRaises(TypeError, _struct.Struct, "I")
        self.assertRaises(TypeError, _struct.Struct, "")
        self.assertRaises(TypeError, _struct.Struct, 1)
        self.assertRaises(TypeError, _struct.Struct, ())
        self.assertRaises(TypeError, _struct.Struct, [])

    def test_sizeof(self):
        # Test _struct.Struct.sizeof
        self.assertEqual(_struct.Struct("i").size, 4)
        self.assertEqual(_struct.Struct("i").size, struct.calcsize("i"))
        self.assertEqual(_struct.Struct("ii").size,
