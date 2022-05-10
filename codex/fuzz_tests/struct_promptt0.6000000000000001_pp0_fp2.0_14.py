import _struct
# Test _struct.Struct
from test import test_support

class StructTest(unittest.TestCase):

    def test_format_size(self):
        struct._clearcache()
        for format, size in (('x', 1),
                             ('c', 1), ('b', 1), ('B', 1),
                             ('h', 2), ('H', 2),
                             ('i', 4), ('I', 4),
                             ('l', 4), ('L', 4),
                             ('q', 8), ('Q', 8),
                             ('f', 4), ('d', 8)):
            s = struct.Struct(format)
            self.assertEqual(s.size, size)
            self.assertEqual(s.format, format)
            self.assertEqual(struct.calcsize(format), size)

    def test_unpack(self):
        struct._clearcache()
        s = struct.Struct('i')
        for fmt, input, expected in (('i', b'\x01\x00\x00\x00', 1),
                                     ('i',
