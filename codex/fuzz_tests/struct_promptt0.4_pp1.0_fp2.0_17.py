import _struct
# Test _struct.Struct
import unittest
from test import support

class StructTest(unittest.TestCase):

    def test_struct(self):
        s = _struct.Struct('i')
        self.assertEqual(s.size, _struct.calcsize('i'))
        self.assertEqual(s.format, 'i')
        self.assertEqual(s.pack(1), b'\x01\x00\x00\x00')
        self.assertEqual(s.unpack(b'\x01\x00\x00\x00'), (1,))
        self.assertEqual(s.pack_into(bytearray(12), 4, 1), None)
        self.assertEqual(bytearray(b'\x00'*4 + b'\x01\x00\x00\x00' + b'\x00'*4),
                         bytearray(b'\x00'*12))
        self.assertEqual(s.unpack_from(b'\x00'*4 + b
