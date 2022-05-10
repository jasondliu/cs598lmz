import _struct
# Test _struct.Struct

import unittest
import sys

class StructTest(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(_struct.Struct('i').size, 4)
        self.assertEqual(_struct.Struct('ii').size, 8)
        self.assertEqual(_struct.Struct('i').pack(12345), b'\x39\x30\x00\x00')
        self.assertEqual(_struct.Struct('i').unpack(b'\x39\x30\x00\x00'), (12345,))
        self.assertEqual(_struct.Struct('i').unpack_from(b'\x39\x30\x00\x00', 0), (12345,))
        self.assertEqual(_struct.Struct('i').unpack_from(b'\x39\x30\x00\x00', 0), (12345,))
