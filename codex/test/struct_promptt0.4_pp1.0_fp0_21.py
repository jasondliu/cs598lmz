import _struct
# Test _struct.Struct.

import test.support
import unittest

class StructTest(unittest.TestCase):
    def test_struct(self):
        s = _struct.Struct('i')
        self.assertEqual(s.size, 4)
        self.assertEqual(s.pack(12345), b'\x39\x30\x00\x00')
        self.assertEqual(s.unpack(b'\x39\x30\x00\x00'), (12345,))

        s = _struct.Struct('ii')
        self.assertEqual(s.size, 8)
        self.assertEqual(s.pack(54321, 12345), b'\x39\x30\x00\x00\x39\x30\x00\x00')
        self.assertEqual(s.unpack(b'\x39\x30\x00\x00\x39\x30\x00\x00'), (54321, 12345))

    def test_unpack_from(self):
        s
