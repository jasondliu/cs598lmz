import _struct
# Test _struct.Struct.

import unittest
import sys
import struct

class StructTest(unittest.TestCase):

    def test_format_size(self):
        self.assertEqual(_struct.calcsize('i'), 4)
        self.assertEqual(_struct.calcsize('ii'), 8)
        self.assertEqual(_struct.calcsize('i'*100), 400)
        self.assertEqual(_struct.calcsize('i'*1000), 4000)
        self.assertEqual(_struct.calcsize('i'*10000), 40000)

    def test_pack(self):
        self.assertEqual(_struct.pack('i', 1), b'\x01\x00\x00\x00')
        self.assertEqual(_struct.pack('i', 0), b'\x00\x00\x00\x00')
        self.assertEqual(_struct.pack('i', -1), b'\xff\xff\xff\xff')
        self.assertEqual(_struct.pack('i', -2), b'\
