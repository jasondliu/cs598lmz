import _struct
# Test _struct.Struct.

import struct
import sys
import unittest
from test import support


class StructTest(unittest.TestCase):
    def test_constructor(self):
        self.assertRaises(TypeError, _struct.Struct)
        self.assertRaises(TypeError, _struct.Struct, b'abc', b'def')
        self.assertRaises(TypeError, _struct.Struct, 'abc', 'def')
        self.assertRaises(TypeError, _struct.Struct, 'abc', 10)
        self.assertRaises(TypeError, _struct.Struct, 'abc', 0)
        self.assertRaises(TypeError, _struct.Struct, 'abc', -1)
        self.assertRaises(TypeError, _struct.Struct, 'abc', 1.0)
        self.assertRaises(TypeError, _struct.Struct, 'abc', 1j)
        self.assertRaises(ValueError, _struct.Struct, 'abc', '@')
        self.assertRaises(ValueError, _struct.Struct, 'abc', '=')
