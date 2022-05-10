import _struct
# Test _struct.Struct
import _struct

class StructTest(unittest.TestCase):

    def test_format(self):
        # Test the format character
        for format in 'xbhilfd':
            s = _struct.Struct(format)
            self.assertEqual(s.format, format)
        for format in '@=<>!':
            s = _struct.Struct(format)
            self.assertEqual(s.format, '@')
        for format in 'PQ':
            s = _struct.Struct(format)
            self.assertEqual(s.format, 'P')
        self.assertRaises(TypeError, _struct.Struct, 'Z')

    def test_size(self):
        # Test the size attribute
        for format, size in [('x', 1),
                             ('b', 1),
                             ('h', 2),
                             ('i', 4),
                             ('l', 4),
                             ('f', 4),
                             ('d', 8),
                             ('P', _struct.calcsize('P')),
                
