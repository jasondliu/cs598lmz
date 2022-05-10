import _struct
# Test _struct.Struct

class StructTest(unittest.TestCase):
    def test_unpack(self):
        s = _struct.Struct('i')
        self.assertEqual(s.size, 4)
        self.assertEqual(s.pack(10), b'\n\x00\x00\x00')
        self.assertEqual(s.unpack(b'\n\x00\x00\x00'), (10,))
        self.assertRaises(TypeError, s.unpack, b'\n\x00\x00')

    def test_unpack_from(self):
        s = _struct.Struct('i')
        self.assertEqual(s.size, 4)
        self.assertEqual(s.pack(10), b'\n\x00\x00\x00')
        buf = bytearray(b'\x00\x00\x00\x00\n\x00\x00\x00')
        self.assertEqual(s.unpack_from(buf, 4), (10,
