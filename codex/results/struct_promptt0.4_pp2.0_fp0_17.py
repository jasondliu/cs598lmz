import _struct
# Test _struct.Struct

def test_struct_error():
    raises(TypeError, _struct.Struct)
    raises(TypeError, _struct.Struct, 'x', 'y')
    raises(TypeError, _struct.Struct, 'x', 'y', 'z')
    raises(TypeError, _struct.Struct, 'x', 'y', 'z', 't')
    raises(TypeError, _struct.Struct, 'x', 'y', 'z', 't', 'u')
    raises(TypeError, _struct.Struct, 'x', 'y', 'z', 't', 'u', 'v')
    raises(TypeError, _struct.Struct, 'x', 'y', 'z', 't', 'u', 'v', 'w')
    raises(TypeError, _struct.Struct, 'x', 'y', 'z', 't', 'u', 'v', 'w', 'A')
    raises(TypeError, _struct.Struct, 'x', 'y', 'z', 't', 'u', 'v', 'w', 'A', 'B')
    raises(TypeError,
