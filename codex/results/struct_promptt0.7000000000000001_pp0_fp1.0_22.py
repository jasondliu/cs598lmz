import _struct
# Test _struct.Struct and format string.
class StructTest(unittest.TestCase):
    def test_struct(self):
        for code in 'bBhHiIlLfd':
            s = _struct.Struct(code)
            self.assertEqual(s.size, struct.calcsize(code))
            self.assertEqual(s.format, code)
        # Try it with some non-native sizes
        if sys.byteorder == "little":
            s = _struct.Struct('@2i')
            self.assertEqual(s.size, 8)
            self.assertEqual(s.format, '@2i')
            s = _struct.Struct('=2i')
            self.assertEqual(s.size, 8)
            self.assertEqual(s.format, '=2i')
            s = _struct.Struct('<2i')
            self.assertEqual(s.size, 8)
            self.assertEqual(s.format, '<2i')
            s = _struct.Struct('>2i')
            self.assert
