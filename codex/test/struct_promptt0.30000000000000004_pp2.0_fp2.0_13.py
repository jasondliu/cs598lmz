import _struct
# Test _struct.Struct

class StructTest(unittest.TestCase):

    def test_struct(self):
        st = _struct.Struct('i')
        self.assertEqual(st.size, 4)
        self.assertEqual(st.pack(12345), b'\x39\x30\x00\x00')
        self.assertEqual(st.unpack(b'\x39\x30\x00\x00'), (12345,))
        self.assertEqual(st.unpack_from(b'\x39\x30\x00\x00'), (12345,))
        self.assertEqual(st.unpack_from(b'\x39\x30\x00\x00', 1), ())
        self.assertEqual(st.unpack_from(b'\x39\x30\x00\x00', 2), ())
