import _struct
# Test _struct.Struct
class StructTestCase(unittest.TestCase):
    def test_struct(self):
        s = _struct.Struct('i')
        self.assertEqual(s.size, 4)
        self.assertEqual(s.pack(1), b'\x01\x00\x00\x00')
        self.assertEqual(s.unpack(b'\x01\x00\x00\x00'), (1,))
        self.assertEqual(s.unpack_from(b'\x00'*4+b'\x01\x00\x00\x00'), (1,))
        self.assertEqual(s.pack_into(bytearray(8), 4, 1), None)
        self.assertEqual(bytes(bytearray(8)), b'\x00'*8)
        self.assertRaises(TypeError, s.pack)
        self.assertRaises(TypeError, s.pack, 1, 2)
        self.assertRaises(TypeError, s.pack_into, b
