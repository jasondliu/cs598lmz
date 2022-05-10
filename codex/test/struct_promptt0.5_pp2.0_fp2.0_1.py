import _struct
# Test _struct.Struct

import unittest
from test import support

class StructTestCase(unittest.TestCase):

    def test_big_endian(self):
        # test big endian
        s = _struct.Struct('>i')
        self.assertEqual(s.size, 4)
        self.assertEqual(s.pack(1), b'\0\0\0\1')
        self.assertEqual(s.unpack(b'\0\0\0\1'), (1,))
        self.assertEqual(s.unpack_from(b'xxxx\0\0\0\1', 4), (1,))

    def test_little_endian(self):
        # test little endian
        s = _struct.Struct('<i')
        self.assertEqual(s.size, 4)
        self.assertEqual(s.pack(1), b'\1\0\0\0')
        self.assertEqual(s.unpack(b'\1\0\0\0'), (1,))
       
