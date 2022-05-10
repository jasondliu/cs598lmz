import _struct
# Test _struct.Struct, both with and without existing
class test_Struct(unittest.TestCase):
    def test_format(self):
        # All valid format characters should be accepted
        for t in 'xbBhHiIlLfd':
            st = _struct.Struct(t)
            self.assertEqual(st.format, t)

    def test_size(self):
        for t, s in (
            ('x', 1),
            ('b', 1),
            ('b', 1),
            ('h', 2),
            ('H', 2),
            ('i', 4),
            ('l', 4),
            ('L', 4),
            ('f', 4),
            ('d', 8)):
            st = _struct.Struct(t)
            self.assertEqual(st.size, s)

    def test_pack(self):
        # Single character format
        st = _struct.Struct('x')
        self.assertEqual(st.pack(), b'\0')
        self.assertEqual(st.pack(42), b'\0')
        # Single
