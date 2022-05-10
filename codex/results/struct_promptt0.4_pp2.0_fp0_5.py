import _struct
# Test _struct.Struct

def test_struct_error(self):
    # Issue #17078: _struct.Struct("") should raise ValueError.
    self.assertRaises(ValueError, _struct.Struct, "")
    self.assertRaises(ValueError, _struct.Struct, "I I")
    self.assertRaises(ValueError, _struct.Struct, "I I ")
    self.assertRaises(ValueError, _struct.Struct, "I I I")
    self.assertRaises(ValueError, _struct.Struct, "I I I ")
    self.assertRaises(ValueError, _struct.Struct, "I I I I")
    self.assertRaises(ValueError, _struct.Struct, "I I I I ")
    self.assertRaises(ValueError, _struct.Struct, "I I I I I")
    self.assertRaises(ValueError, _struct.Struct, "I I I I I ")
    self.assertRaises(ValueError, _struct.Struct, "I I I I I I")
    self.assertRaises
