import _struct
# Test _struct.Struct

class StructTest(unittest.TestCase):
    def test_pack(self):
        st = _struct.Struct('i')
        self.assertEqual(st.pack(1), b'\x01\x00\x00\x00')
        self.assertRaises(TypeError, st.pack, 'hello')
        self.assertRaises(TypeError, st.pack, 1, 2, 3)
        self.assertRaises(TypeError, st.pack, 1, 2)
        self.assertRaises(TypeError, st.pack)

    def test_unpack(self):
        st = _struct.Struct('i')
        self.assertEqual(st.unpack(b'\x01\x00\x00\x00'), (1,))
        self.assertRaises(TypeError, st.unpack, 'hello')
        self.assertRaises(TypeError, st.unpack, b'\x01\x00\x00\x00', 2)
        self.assertRaises(TypeError, st.unpack,
