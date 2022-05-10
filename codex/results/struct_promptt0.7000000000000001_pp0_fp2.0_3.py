import _struct
# Test _struct.Struct.unpack

import sys
import unittest

from test import support


class StructTest(unittest.TestCase):
    def test_unpack(self):
        s = _struct.Struct('ii')
        self.assertEqual(s.unpack(b'\x00\x00\x00\x01\x00\x00\x00\x02'),
                         (1, 2))
        self.assertEqual(s.unpack(memoryview(b'\x00\x00\x00\x01\x00\x00\x00\x02')),
                         (1, 2))

    def test_unpack_too_short(self):
        s = _struct.Struct('ii')
        self.assertRaises(TypeError, s.unpack, b'\x00\x00\x00\x01\x00\x00\x00')
        self.assertRaises(TypeError, s.unpack, memoryview(b'\x00\x00\x00\x01\x00\x00\x
