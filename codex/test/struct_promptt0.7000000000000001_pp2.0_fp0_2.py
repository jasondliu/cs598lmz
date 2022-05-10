import _struct
# Test _struct.Struct
import unittest
import sys

class StructTestCase(unittest.TestCase):

    def test_Struct(self):
        self.assertEqual(_struct.Struct('i').size, 4)
        self.assertEqual(_struct.Struct('i').pack(42), b'*\x00\x00\x00')
        self.assertEqual(_struct.Struct('i').unpack(b'*\x00\x00\x00'), (42,))
        self.assertEqual(_struct.Struct('i').unpack_from(b'\x00\x00\x00*', 0), (42,))
        self.assertEqual(_struct.Struct('i').unpack_from(b'\x00\x00\x00*', 0), (42,))
        self.assertEqual(_struct.Struct('i').unpack_from(b'\x00\x00\x00*', 1), (42,))
