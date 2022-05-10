import _struct
# Test _struct.Struct
class TestStruct(unittest.TestCase):
    def test_constructor(self):
        self.assertRaises(TypeError, _struct.Struct)
        self.assertRaises(TypeError, _struct.Struct, 'abc', 'def')
        self.assertRaises(TypeError, _struct.Struct, 'abc', 'def', 'ghi')
        self.assertRaises(TypeError, _struct.Struct, 'abc', 'def', 'ghi',
            'jkl')
        self.assertRaises(TypeError, _struct.Struct, 'abc', 'def', 'ghi',
            'jkl', 'mno')
        self.assertRaises(TypeError, _struct.Struct, 'abc', 'def', 'ghi',
            'jkl', 'mno', 'pqr')
        self.assertRaises(TypeError, _struct.Struct, 'abc', 'def', 'ghi',
            'jkl', 'mno', 'pqr', 'stu')
        self.assertRaises(TypeError, _struct.Struct,
