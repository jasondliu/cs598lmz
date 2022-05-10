import _struct
# Test _struct.Struct

class StructTestCase(unittest.TestCase):

    def test_struct_with_format(self):
        # Test struct.Struct
        s = _struct.Struct('hhl')
        self.assertEqual(s.size, 8)
        self.assertEqual(s.pack(1, 2, 3), b'\x01\x00\x02\x00\x00\x00\x00\x03')
        self.assertEqual(s.unpack(b'\x01\x00\x02\x00\x00\x00\x00\x03'), (1, 2, 3))
        self.assertEqual(s.unpack_from(b'\xff\xfe\xfd\xfc\xff\x00\x00\x03', 4), (255, 3))
        self.assertEqual(s.pack_into(b'\x00'*8, 0, 1, 2, 3), None)
        self.assertEqual(b'\x01\x00\x02\x00\x
