import _struct
# Test _struct.Struct

class TestStruct:

    def test_basics(self):
        # Test _struct.Struct
        st = _struct.Struct('i')
        self.assertRaises(TypeError, st.__init__, 'ii')
        st = _struct.Struct('ii')
        self.assertEqual(st.size, 8)
        self.assertEqual(st.format, 'ii')
        self.assertRaises(TypeError, st.pack, None)
        self.assertRaises(TypeError, st.pack, 'a')
        self.assertRaises(TypeError, st.pack, 'abc')
        self.assertRaises(TypeError, st.pack, 'abcd')
        self.assertRaises(TypeError, st.pack, 'abcde')
        self.assertRaises(TypeError, st.pack, 'abcdef')
        self.assertRaises(TypeError, st.pack, 'abcdefg')
        self.assertRaises(TypeError, st.pack, 'abcdefgh')
