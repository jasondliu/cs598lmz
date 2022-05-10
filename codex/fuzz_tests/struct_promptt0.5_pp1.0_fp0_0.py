import _struct
# Test _struct.Struct
class TestStruct(unittest.TestCase):
    def test_creation(self):
        self.assertRaises(TypeError, _struct.Struct)
        self.assertRaises(TypeError, _struct.Struct, 'abc', 'def')
        self.assertRaises(TypeError, _struct.Struct, 'abc', 'def', 'ghi')
        self.assertRaises(TypeError, _struct.Struct, 'abc', 42)
        self.assertRaises(TypeError, _struct.Struct, 'abc', 42, 'def')
        self.assertRaises(TypeError, _struct.Struct, 'abc', 42, 'def', 'ghi')
        self.assertRaises(TypeError, _struct.Struct, 'abc', 42, 'def', 'ghi',
                          'jkl')
        self.assertRaises(TypeError, _struct.Struct, 'abc', 42, 'def', 'ghi',
                          'jkl', 'mno')
        self.assertRaises(TypeError, _struct.Struct, 'abc', 42, 'def',
