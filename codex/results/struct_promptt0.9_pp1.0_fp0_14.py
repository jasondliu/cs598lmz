import _struct
# Test _struct.Struct(b'f')

class _struct_test_suite(unittest.TestCase):

    format = '@P'
    size = 8
    def test_Struct(self):
        import _struct
        st = _struct.Struct(self.format)
        self.assertEqual(st.format, self.format)
        self.assertEqual(st.size, self.size)
        self.assertEqual(st.__doc__, 'Compiled from ' + repr(self.format))
        self.assertRaises(ValueError, st.__new__, _struct.Struct)
        self.assertRaises(TypeError, st.__new__, _struct.Struct, b'', 0, 0)
        self.assertRaises(ValueError, _struct.Struct, 'xyz')

    def test_unpack(self):
        import _struct
        st = _struct.Struct(self.format)
        self.assertRaises(TypeError, st.unpack)
        self.assertRaises(TypeError, st.unpack, b'')

