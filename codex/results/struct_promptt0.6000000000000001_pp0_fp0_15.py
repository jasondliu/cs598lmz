import _struct
# Test _struct.Struct

import sys
import test.support
import unittest

import _testbuffer

class StructTestCase(unittest.TestCase):
    def test_struct(self):
        # Test _struct.Struct object
        s = _struct.Struct('i')
        self.assertEqual(s.size, _struct.calcsize('i'))
        self.assertEqual(s.format, 'i')
        self.assertEqual(s.pack(12345), b'\x39\x30\x00\x00')
        self.assertEqual(s.unpack(b'\x39\x30\x00\x00'), (12345,))
        self.assertEqual(s.unpack_from(b'\x39\x30\x00\x00'), (12345,))
        self.assertRaises(TypeError, s.pack)
        self.assertRaises(TypeError, s.pack, 1, 2)
        self.assertRaises(TypeError, s.pack, 1, 2, 3)
        self
