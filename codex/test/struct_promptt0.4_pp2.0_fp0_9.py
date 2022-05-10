import _struct
# Test _struct.Struct.

import unittest

class StructTest(unittest.TestCase):
    def test_struct(self):
        s = _struct.Struct('i')
        self.assertEqual(s.size, 4)
        self.assertEqual(s.pack(1), b'\x01\x00\x00\x00')
        self.assertEqual(s.unpack(b'\x01\x00\x00\x00'), (1,))
        self.assertEqual(s.unpack_from(b'\xff\x00\x00\x00\x01\x00\x00\x00', 1), (1,))
        self.assertEqual(s.unpack_from(bytearray(b'\xff\x00\x00\x00\x01\x00\x00\x00'), 1), (1,))

    def test_struct_format(self):
        s = _struct.Struct('i')
        self.assertEqual(s.format, 'i')
