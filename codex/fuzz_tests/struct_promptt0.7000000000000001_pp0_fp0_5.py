import _struct
# Test _struct.Struct
import struct
import unittest
import sys


class StructTestCase(unittest.TestCase):

    def test_format_size(self):
        self.assertEqual(_struct.calcsize('c'), struct.calcsize('c'))

        self.assertEqual(_struct.calcsize('bBhHiIlLqQfd'), struct.calcsize(
            'bBhHiIlLqQfd'))
        self.assertEqual(_struct.calcsize('P'), struct.calcsize('P'))
        self.assertEqual(_struct.calcsize('s'), struct.calcsize('s'))
        self.assertEqual(_struct.calcsize('p'), struct.calcsize('p'))
        self.assertEqual(_struct.calcsize('7s'), struct.calcsize('7s'))

    def test_pack(self):
        fmt = 'hhl5s'
        buf = _struct.pack(fmt, 1, 2, 3, b'4567')
        self.assertEqual
