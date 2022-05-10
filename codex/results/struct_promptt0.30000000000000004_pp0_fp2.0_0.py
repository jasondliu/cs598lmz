import _struct
# Test _struct.Struct.format

def test_format():
    # Make sure format string is checked
    raises(TypeError, _struct.Struct, "")
    raises(TypeError, _struct.Struct, "i")
    raises(TypeError, _struct.Struct, "ii")
    raises(TypeError, _struct.Struct, "ii", 1)
    raises(TypeError, _struct.Struct, "ii", 1, 2)
    raises(TypeError, _struct.Struct, "ii", 1, 2, 3)
    raises(TypeError, _struct.Struct, "ii", 1, 2, 3, 4)
    raises(TypeError, _struct.Struct, "ii", 1, 2, 3, 4, 5)
    raises(TypeError, _struct.Struct, "ii", 1, 2, 3, 4, 5, 6)
    raises(TypeError, _struct.Struct, "ii", 1, 2, 3, 4, 5, 6, 7)
    raises(TypeError, _struct.Struct, "ii", 1, 2, 3, 4, 5, 6, 7, 8)
   
