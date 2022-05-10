import _struct
# Test _struct.Struct
import unittest
from test import support

class StructTestCase(unittest.TestCase):
    def test_format(self):
        self.assertEqual(_struct.calcsize('h'), 2)
        self.assertEqual(_struct.calcsize('hhh'), 6)
        self.assertEqual(_struct.calcsize('hhhh'), 8)
        self.assertRaises(TypeError, _struct.calcsize, 'z')
        self.assertRaises(TypeError, _struct.calcsize, 'hhhhhh')
        self.assertRaises(TypeError, _struct.calcsize, 'hhh', 0, 1, 2)

    def test_unpack(self):
        self.assertEqual(_struct.unpack('>hhh', b'\x00\x00\x01\x00\x00\x02'),
                         (1, 0, 2))
        self.assertEqual(_struct.pack('>hhh', 1, 0, 2),
                         b'\x00\x00\x01\x00\x00\x02
