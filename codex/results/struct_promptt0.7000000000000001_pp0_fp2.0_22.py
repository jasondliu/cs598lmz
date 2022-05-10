import _struct
# Test _struct.Struct.


class StructTest(unittest.TestCase):
    def test_unpack(self):
        s = _struct.Struct(b'hhl')
        self.assertEqual(s.size, 8)
        self.assertEqual(s.pack(1, 2, 3), b'\x01\x00\x02\x00\x00\x00\x00\x03')
        self.assertEqual(s.unpack(b'\x01\x00\x02\x00\x00\x00\x00\x03'), (1, 2, 3))
        self.assertRaises(TypeError, s.unpack, b'hi')
        self.assertRaises(TypeError, s.unpack, b'hi', 0, 1)
        self.assertRaises(TypeError, s.unpack, b'hi', 0, 1, 0)

    def test_iter_unpack(self):
        s = _struct.Struct(b'hhl')
        self.assertEqual(s.iter_unpack(b
