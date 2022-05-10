import _struct
# Test _struct.Struct.

import unittest

class StructTestCase(unittest.TestCase):
    def test_basics(self):
        self.assertEqual(_struct.Struct('i').size, 4)
        self.assertEqual(_struct.Struct('ii').size, 8)
        self.assertEqual(_struct.Struct('i').pack(42), b'*\x00\x00\x00')
        self.assertEqual(_struct.Struct('i').pack(42, 'little'), b'\x00\x00\x00*')
        self.assertEqual(_struct.Struct('i').pack(42, 'big'), b'*\x00\x00\x00')
        self.assertEqual(_struct.Struct('i').unpack(b'*\x00\x00\x00'), (42,))
        self.assertEqual(_struct.Struct('i').unpack(b'\x00\x00\x00*'), (42,))
        self.assertEqual(_struct.Struct('i').unpack(b'*\x
