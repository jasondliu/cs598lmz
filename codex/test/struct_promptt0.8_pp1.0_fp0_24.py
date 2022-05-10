import _struct
# Test _struct.Struct


class StructTest(unittest.TestCase):

    def test_struct(self):
        self.assertEqual(repr(_struct.Struct('@')), "Struct('@')")
        self.assertEqual(repr(_struct.Struct('=')), "Struct('=')")
        self.assertEqual(repr(_struct.Struct('P')), "Struct('P')")

    @support.cpython_only
    def test_maximum_size(self):
        max_size = 2**31 - 1
        s = _struct.Struct('@' + str(max_size))
        self.assertEqual(s.size, max_size)
        self.assertEqual(s.format, '@' + str(max_size))
        s2 = _struct.Struct('@' + str(max_size) + 'p')
        self.assertEqual(s2.format, '@' + str(max_size) + 'p')
