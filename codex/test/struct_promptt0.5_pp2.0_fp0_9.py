import _struct
# Test _struct.Struct()
class TestStruct(unittest.TestCase):

    def test_struct(self):
        self.assertEqual(_struct.Struct('i').size, 4)
        self.assertEqual(_struct.Struct('i').pack(1), b'\x01\x00\x00\x00')
        self.assertEqual(_struct.Struct('i').unpack(b'\x01\x00\x00\x00'), (1,))
        self.assertEqual(_struct.Struct('i').pack_into(b'\x00' * 4, 0, 1), None)
        self.assertEqual(b'\x01\x00\x00\x00', b'\x00' * 4)
        self.assertEqual(_struct.Struct('i').unpack_from(b'\x01\x00\x00\x00', 0), (1,))
