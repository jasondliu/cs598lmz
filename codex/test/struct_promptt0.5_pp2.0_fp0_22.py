import _struct
# Test _struct.Struct

class StructTest(unittest.TestCase):

    def test_struct(self):
        self.assertEqual(_struct.Struct('i').size, 4)
        self.assertEqual(_struct.Struct('i').pack(10), b'\n\x00\x00\x00')
        self.assertEqual(_struct.Struct('i').unpack(b'\n\x00\x00\x00'), (10,))
        self.assertEqual(_struct.Struct('i').unpack_from(b'\x00'*16, 12), (10,))
        self.assertEqual(_struct.Struct('i').unpack_from(bytearray(b'\x00'*16), 12), (10,))

        self.assertEqual(_struct.Struct('i').iter_unpack(b'\n\x00\x00\x00'), [(10,)])
