import _struct
# Test _struct.Struct

# Test packing and unpacking of various types.

import sys
import unittest
import struct

from test import support

class StructTest(unittest.TestCase):

    def test_bool(self):
        s = _struct.Struct('?')
        self.assertEqual(s.size, 1)
        self.assertEqual(s.pack(True), b'\x01')
        self.assertEqual(s.unpack(b'\x01'), (True,))
        self.assertEqual(s.unpack(b'\x00'), (False,))
        self.assertEqual(s.unpack_from(b'\x01'), (True,))
        self.assertEqual(s.unpack_from(b'\x00'), (False,))

    def test_byte(self):
        s = _struct.Struct('b')
        self.assertEqual(s.size, 1)
        self.assertEqual(s.pack(0), b'\x00')
        self.assertEqual(s
