import _struct
# Test _struct.Struct.__repr__

class TestStructRepr(unittest.TestCase):
    def test_repr(self):
        s = _struct.Struct(b'f')
        self.assertEqual(repr(s), 'Struct(b\'f\')')

        s = _struct.Struct('df')
        self.assertEqual(repr(s), 'Struct(\'df\')')

        s = _struct.Struct(u'df')
        self.assertEqual(repr(s), 'Struct(\'df\')')

class TestStructFormats(unittest.TestCase):
    def test_misc_formats(self):
        for code in 'cbBhHiIlLfdspP':
            _struct.Struct(code)

