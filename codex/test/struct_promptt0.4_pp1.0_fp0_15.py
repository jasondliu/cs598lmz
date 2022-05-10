import _struct
# Test _struct.Struct.__new__

class StructTest(unittest.TestCase):
    def test_format(self):
        self.assertRaises(TypeError, _struct.Struct, 1)
        self.assertRaises(TypeError, _struct.Struct, 1, 2, 3)
        self.assertRaises(TypeError, _struct.Struct, 'abc', 'def')
        self.assertRaises(TypeError, _struct.Struct, 'abc', '=')
        self.assertRaises(TypeError, _struct.Struct, 'abc', '=', 'def')
        self.assertRaises(TypeError, _struct.Struct, 'abc', '=', 'def', 'ghi')
        self.assertRaises(TypeError, _struct.Struct, 'abc', '=', 'def', 'ghi', 'jkl')
        self.assertRaises(TypeError, _struct.Struct, 'abc', '=', 'def', 'ghi', 'jkl', 'mno')

        self.assertRaises(ValueError, _struct.Struct, '')
