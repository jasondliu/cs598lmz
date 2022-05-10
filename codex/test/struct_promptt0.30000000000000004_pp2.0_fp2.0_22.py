import _struct
# Test _struct.Struct.__new__

def test_new(self):
    self.assertRaises(TypeError, _struct.Struct)
    self.assertRaises(TypeError, _struct.Struct, '', ())
    self.assertRaises(TypeError, _struct.Struct, '', (1,))
    self.assertRaises(TypeError, _struct.Struct, '', (1, 2))
    self.assertRaises(TypeError, _struct.Struct, '', (1, 2, 3))
    self.assertRaises(TypeError, _struct.Struct, '', (1, 2, 3, 4))
    self.assertRaises(TypeError, _struct.Struct, '', (1, 2, 3, 4, 5))
    self.assertRaises(TypeError, _struct.Struct, '', (1, 2, 3, 4, 5, 6))
    self.assertRaises(TypeError, _struct.Struct, '', (1, 2, 3, 4, 5, 6, 7))
