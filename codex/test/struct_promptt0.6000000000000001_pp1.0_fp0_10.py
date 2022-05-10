import _struct
# Test _struct.Struct


class TestStruct(unittest.TestCase):

    def test_pack_unpack(self):
        s = _struct.Struct('l')
        self.assertEqual(s.pack(0x12345678), b'xV\x12\x34')
        self.assertEqual(s.unpack(b'xV\x12\x34'), (0x12345678,))

    def test_pack_unpack_big_endian(self):
        s = _struct.Struct('>l')
        self.assertEqual(s.pack(0x12345678), b'\x12\x34Vx')
        self.assertEqual(s.unpack(b'\x12\x34Vx'), (0x12345678,))

    def test_pack_unpack_little_endian(self):
        s = _struct.Struct('<l')
        self.assertEqual(s.pack(0x12345678), b'xV\x12\x34')
