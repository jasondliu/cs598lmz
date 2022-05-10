import _struct
# Test _struct.Struct.

import unittest

class StructTest(unittest.TestCase):

    def test_struct(self):
        self.assertEqual(_struct.calcsize('i'), 4)
        self.assertEqual(_struct.calcsize('ii'), 8)
        self.assertEqual(_struct.calcsize('iP'), 8)

        self.assertEqual(_struct.pack('i', 1), b'\x01\x00\x00\x00')
        self.assertEqual(_struct.pack('ii', 1, 2), b'\x01\x00\x00\x00\x02\x00\x00\x00')
        self.assertEqual(_struct.pack('iP', 1, 2), b'\x01\x00\x00\x00\x02\x00\x00\x00')

        self.assertEqual(_struct.unpack('i', b'\x01\x00\x00\x00'), (1,))
