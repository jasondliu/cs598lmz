import _struct
# Test _struct.Struct with standard format strings

class SizesTestCase(unittest.TestCase):
    def test_native(self):
        for code in 'bBhHiIlLfdfsu':
            s = _struct.Struct(code)
            expected = struct.calcsize(code)
            self.assertEqual(s.size, expected)
            self.assertEqual(s.format_size, expected)
            self.assertEqual(s.alignment, expected)
            self.assertEqual(s.format, code)
            self.assertEqual(str(s), '<' + code)
            self.assertEqual(repr(s), '<' + code)

    def test_standard_size(self):
        for code in '@=Q':
            s = _struct.Struct(code)
            expected = struct.calcsize(code)
            self.assertEqual(s.size, expected)
            self.assertEqual(s.format_size, expected)
            self.assertEqual(s.alignment, 1)
            self.
