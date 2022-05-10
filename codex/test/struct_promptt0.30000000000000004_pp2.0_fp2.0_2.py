import _struct
# Test _struct.Struct

# _struct.Struct is a factory that creates classes that can convert between
# Python values and C structs packed into Python strings.

import sys
import unittest
from test import support

class StructTestCase(unittest.TestCase):

    def test_unpack(self):
        # Test the unpack method.
        s = _struct.Struct('i')
        self.assertEqual(s.unpack(b'\x01\x00\x00\x00'), (1,))
        self.assertEqual(s.unpack(b'\x01\x00\x00\x00', 1), (256,))
        self.assertEqual(s.unpack(b'x\x00\x00\x00\x01\x00\x00\x00', 1), (1,))
        self.assertRaises(TypeError, s.unpack, 'abc')
        self.assertRaises(TypeError, s.unpack, b'abc')
