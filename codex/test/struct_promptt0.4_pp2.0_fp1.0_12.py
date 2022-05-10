import _struct
# Test _struct.Struct

class StructTest(unittest.TestCase):

    def test_struct(self):
        self.assertEqual(_struct.Struct('i').size, 4)
        self.assertEqual(_struct.Struct('i').pack(42), b'*\x00\x00\x00')
        self.assertEqual(_struct.Struct('i').unpack(b'*\x00\x00\x00'), (42,))
        self.assertEqual(_struct.Struct('i').unpack_from(b'\x00\x00\x00*'), (42,))
        self.assertEqual(_struct.Struct('i').unpack_from(b'\x00\x00\x00*', 1), ())
        self.assertEqual(_struct.Struct('i').unpack_from(b'\x00\x00\x00*', 4), ())
        self.assertEqual(_struct.Struct('i').unpack_from(b'\x00\x00\x00*', 100), ())
