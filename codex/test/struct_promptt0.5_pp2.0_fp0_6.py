import _struct
# Test _struct.Struct
class StructTestCase(unittest.TestCase):

    def test_struct_error(self):
        self.assertRaises(TypeError, _struct.Struct)
        self.assertRaises(TypeError, _struct.Struct, b'abc', b'def')
        self.assertRaises(TypeError, _struct.Struct, b'abc', 1, 2, 3)
        self.assertRaises(TypeError, _struct.Struct, b'abc', 1, b'def')
        self.assertRaises(TypeError, _struct.Struct, b'abc', 1, 2, b'def')
        self.assertRaises(ValueError, _struct.Struct, b'z')
        self.assertRaises(ValueError, _struct.Struct, b'abcdefgh')
        self.assertRaises(ValueError, _struct.Struct, b'abcdefghi')
        self.assertRaises(ValueError, _struct.Struct, b'abcdefghij')
