import _struct
# Test _struct.Struct.

import test.support
import unittest

class StructTest(unittest.TestCase):

    def test_struct_unpack(self):
        s = _struct.Struct('i')
        self.assertEqual(s.size, 4)
        self.assertEqual(s.unpack(b'\x01\x00\x00\x00'), (1,))
        self.assertEqual(s.unpack(b'\x01\x00\x00\x00'*2), (1, 1))

        s = _struct.Struct('2i')
        self.assertEqual(s.size, 8)
        self.assertEqual(s.unpack(b'\x01\x00\x00\x00\x02\x00\x00\x00'), (1, 2))

        s = _struct.Struct('2i2f')
        self.assertEqual(s.size, 16)
        self.assertEqual(s.unpack(b'\x01\x00\x00\x00
