import _struct
# Test _struct.Struct

import unittest

class StructTestCase(unittest.TestCase):

    def test_format_size(self):
        self.assertEqual(_struct.calcsize(''), 0)
        self.assertEqual(_struct.calcsize('i'), 4)
        self.assertEqual(_struct.calcsize('ii'), 8)
        self.assertEqual(_struct.calcsize('iii'), 12)

    def test_pack(self):
        self.assertEqual(_struct.pack('i', 1), b'\x01\x00\x00\x00')
        self.assertEqual(_struct.pack('ii', 1, 2), b'\x01\x00\x00\x00\x02\x00\x00\x00')
        self.assertEqual(_struct.pack('iii', 1, 2, 3), b'\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00')

