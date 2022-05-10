import _struct
# Test _struct.Struct()

class _StructTest(unittest.TestCase):

    def test_struct_format(self):
        s = _struct.Struct('bBhHiIlLqQfdspP')
        self.assertEqual(s.format, 'bBhHiIlLqQfdspP')

    def test_struct_format_invalid(self):
        # Invalid format
        self.assertRaises(ValueError, _struct.Struct, 'x')
        self.assertRaises(ValueError, _struct.Struct, 'bxx')
        # Odd-length format
        self.assertRaises(ValueError, _struct.Struct, 'bxxc')
        self.assertRaises(ValueError, _struct.Struct, 'bxxc')
        # Overlapped format
        self.assertRaises(ValueError, _struct.Struct, 'bBxB')
        # Out-of-range values
        self.assertRaises(ValueError, _struct.Struct, '9999')
        self.assertRaises(ValueError, _struct.Struct, 'b999')
