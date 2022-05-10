import _struct
# Test _struct.Struct

class StructTestCase(unittest.TestCase):
    def test_struct_error(self):
        self.assertRaises(ValueError, _struct.Struct, 'z')
        self.assertRaises(ValueError, _struct.Struct, 'P')
        self.assertRaises(ValueError, _struct.Struct, 'P', 'little')
        self.assertRaises(ValueError, _struct.Struct, 'P', 'big')
        self.assertRaises(ValueError, _struct.Struct, 'P', 'native')
        self.assertRaises(ValueError, _struct.Struct, 'P', '<')
        self.assertRaises(ValueError, _struct.Struct, 'P', '>')
        self.assertRaises(ValueError, _struct.Struct, 'P', '=')
        self.assertRaises(ValueError, _struct.Struct, 'P', '!')
        self.assertRaises(TypeError, _struct.Struct, 'P', 0)
        self.assertRaises(TypeError, _struct.Struct, 'P
