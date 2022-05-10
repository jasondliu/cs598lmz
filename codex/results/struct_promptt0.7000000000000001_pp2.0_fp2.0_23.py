import _struct
# Test _struct.Struct
import _struct

class StructTest(unittest.TestCase):
    def setUp(self):
        self.st = _struct.Struct('hhl')

    def test_unpack(self):
        st = self.st
        eq = self.assertEqual
        eq(st.unpack(b'\1\0\0\0\2\0\0\0\3\0\0\0'), (1, 2, 3))
        eq(st.unpack(b'\1\2\0\0\0\0\0\0\0\0\0\0'), (258, 0, 0))
        self.assertRaises(struct.error, st.unpack, b'abc')
        self.assertRaises(struct.error, st.unpack, b'\0\0\0\0')
        self.assertRaises(struct.error, st.unpack, b'\0'*80)

    def test_iter_unpack(self):
        st = self.st
        eq = self.assertEqual
        eq
