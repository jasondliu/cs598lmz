import _struct
# Test _struct.Struct
class StructTest(unittest.TestCase):
    def test_basics(self):
        s = _struct.Struct('i')
        self.assertEqual(s.size, 4)
        self.assertEqual(s.pack(12345), b'\x39\x30\x00\x00')
        self.assertEqual(s.unpack(b'\x39\x30\x00\x00'), (12345,))
        self.assertEqual(s.unpack_from(b'\x00\x00\x00\x00\x39\x30\x00\x00', 4), (12345,))
        self.assertEqual(s.pack_into(b'\x00\x00\x00\x00\x00\x00\x00\x00', 4, 12345), None)
        self.assertEqual(b'\x00\x00\x00\x00\x39\x30\x00\x00',
                         b'\x00\x00\x00\
