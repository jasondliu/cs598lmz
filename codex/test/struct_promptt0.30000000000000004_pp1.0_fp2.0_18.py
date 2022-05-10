import _struct
# Test _struct.Struct

# Test _struct.Struct.__init__
def test_struct_init():
    # Test _struct.Struct.__init__
    # Test _struct.Struct.__init__ with bad format
    raises(TypeError, _struct.Struct, "")
    raises(TypeError, _struct.Struct, "b")
    raises(TypeError, _struct.Struct, "b", "b")
    raises(TypeError, _struct.Struct, "b", "b", "b")
    raises(TypeError, _struct.Struct, "b", "b", "b", "b")
    raises(TypeError, _struct.Struct, "b", "b", "b", "b", "b")
    raises(TypeError, _struct.Struct, "b", "b", "b", "b", "b", "b")
    raises(TypeError, _struct.Struct, "b", "b", "b", "b", "b", "b", "b")
