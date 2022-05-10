import _struct
# Test _struct.Struct

def test_struct_error(self):
    # Verify that a type code passed to Struct() is checked for validity.
    self.assertRaises(ValueError, struct.Struct, 'Z')
    self.assertRaises(ValueError, struct.Struct, 'Z9')
    self.assertRaises(TypeError, struct.Struct, 1)

def test_struct_format(self):
    # Verify the format string passed to Struct() is checked for validity.
    self.assertRaises(TypeError, struct.Struct, 'i', 'ii')
    self.assertRaises(TypeError, struct.Struct, 'P', 'P')
    self.assertRaises(struct.error, struct.Struct, 'i', 'q')
    self.assertRaises(struct.error, struct.Struct, 'i', 'P')
    self.assertRaises(struct.error, struct.Struct, 'i', 'x')
    self.assertRaises(struct.error, struct.Struct, 'i', 'cP')
