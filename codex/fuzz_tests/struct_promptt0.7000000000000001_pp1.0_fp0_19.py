import _struct
# Test _struct.Struct to ensure it can handle formats that contain
# non-native-size types.
class TestStruct(unittest.TestCase):
    def test_struct(self):
        S = _struct.Struct('HhL')
        self.assertEqual(S.size, 10)
        self.assertEqual(S.pack(0x1234, -0x1234, 0x12345678), b'\x12\x34\xfe\xec\x78\x56\x34\x12\x00\x00')
        self.assertEqual(S.pack_into(bytearray(10), 0, 0x1234, -0x1234, 0x12345678), None)
        self.assertEqual(bytearray(b'\x00' * 10), b'\x12\x34\xfe\xec\x78\x56\x34\x12\x00\x00')
        self.assertEqual(S.unpack(b'\x12\x34\xfe\xec\x78\x
