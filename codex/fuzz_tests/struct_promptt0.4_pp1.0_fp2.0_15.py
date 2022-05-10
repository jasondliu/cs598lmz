import _struct
# Test _struct.Struct

import unittest

class StructTest(unittest.TestCase):

    def test_format_size(self):
        self.assertEqual(_struct.calcsize('i'), 4)
        self.assertEqual(_struct.calcsize('iP'), 4 + _struct.calcsize('P'))
        self.assertEqual(_struct.calcsize('iP'), 4 + _struct.calcsize('P'))
        self.assertEqual(_struct.calcsize('iP'), 4 + _struct.calcsize('P'))

    def test_unpack(self):
        self.assertEqual(_struct.unpack('i', b'\x00\x00\x00\x00'), (0,))
        self.assertEqual(_struct.unpack('i', b'\x00\x00\x00\x01'), (1,))
        self.assertEqual(_struct.unpack('i', b'\x00\x00\x00\xff'), (255,))
        self.assertEqual(_struct.
