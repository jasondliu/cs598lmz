import _struct
# Test _struct.Struct
class TestStruct(unittest.TestCase):
    def test_struct_error(self):
        self.assertRaises(TypeError, _struct.Struct)
        self.assertRaises(TypeError, _struct.Struct, 'c', 'c')
        self.assertRaises(TypeError, _struct.Struct, 'abc')
        self.assertRaises(TypeError, _struct.Struct, 'c', 'Z')
        self.assertRaises(TypeError, _struct.Struct, 'c', 'c', 'c')
        self.assertRaises(TypeError, _struct.Struct, 'cx')
        self.assertRaises(TypeError, _struct.Struct, 'cb')
        self.assertRaises(TypeError, _struct.Struct, 'cP')
        self.assertRaises(TypeError, _struct.Struct, 'c8s')
        self.assertRaises(TypeError, _struct.Struct, 'c8sf')
        self.assertRaises(TypeError, _struct.Struct, 'c8sP')
        self.assertRa
