import _struct
# Test _struct.Struct

class StructTestCase(unittest.TestCase):

    def test_struct(self):
        s = _struct.Struct('i')
        self.assertEqual(s.size, _struct.calcsize('i'))
        self.assertEqual(s.pack(0), b'\x00\x00\x00\x00')
        self.assertEqual(s.unpack(b'\x00\x00\x00\x00'), (0,))
        self.assertEqual(s.pack_into(bytearray(b'\x00\x00\x00\x00'), 0, 0), None)
        self.assertEqual(s.unpack_from(b'\x00\x00\x00\x00', 0), (0,))

        self.assertRaises(TypeError, _struct.Struct)
        self.assertRaises(TypeError, _struct.Struct, 'i', 'i')
        self.assertRaises(TypeError, _struct.Struct, 'ii')
        self.assertRa
