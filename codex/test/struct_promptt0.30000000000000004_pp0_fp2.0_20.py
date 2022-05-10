import _struct
# Test _struct.Struct
import unittest
import sys

class StructTest(unittest.TestCase):

    def test_struct(self):
        s = _struct.Struct('i')
        self.assertEqual(s.size, 4)
        self.assertEqual(s.pack(42), b'*\x00\x00\x00')
        self.assertEqual(s.unpack(b'*\x00\x00\x00'), (42,))
        self.assertEqual(s.unpack_from(b'\x00'*4 + b'*\x00\x00\x00'), (42,))
        self.assertEqual(s.unpack_from(b'\x00'*4 + b'*\x00\x00\x00', 4), (42,))
        self.assertEqual(s.unpack_from(b'\x00'*4 + b'*\x00\x00\x00', 5), (0,))
