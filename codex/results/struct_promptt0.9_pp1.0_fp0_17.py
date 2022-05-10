import _struct
# Test _struct.Struct itself
import unittest


class StructTest(unittest.TestCase):

    def test_keywords(self):
        self.assertRaises(TypeError, _struct.Struct, '0')
        self.assertRaises(TypeError, _struct.Struct, '0=')
        self.assertRaises(TypeError, _struct.Struct, '0=0')

    def test_int_one(self):
        s = _struct.Struct('i')
        self.assertEqual(s.size, 4)
        self.assertEqual(s.pack(0), b'\x00\x00\x00\x00')
        self.assertEqual(s.unpack(b'\x00\x00\x00\x00'), (0,))
        for i in 1, 1234, b'+1234':
            self.assertEqual(s.unpack(s.pack(i)), (i,))
            with self.assertRaises(struct.error):
                s.pack_into(b'a' * s.size, 0
