from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'i'
s.size = 4

class TestStruct(unittest.TestCase):

    def test_unpack_from(self):
        buf = bytearray(b'xxxxxx\0\0\0\1')
        self.assertEqual(s.unpack_from(buf, 6), (1,))

    def test_pack_into(self):
        buf = bytearray(b'xxxxxx\0\0\0\0')
        s.pack_into(buf, 6, 1)
        self.assertEqual(buf, b'xxxxxx\0\0\0\1')

    def test_pack_into_with_offset(self):
        buf = bytearray(b'xxxxxx\0\0\0\0')
        s.pack_into(buf, 6, 1, 1)
        self.assertEqual(buf, b'xxxxxx\0\0\0\0')

