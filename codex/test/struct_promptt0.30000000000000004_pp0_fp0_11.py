import _struct
# Test _struct.Struct()

def test_struct_error():
    raises(TypeError, _struct.Struct)
    raises(TypeError, _struct.Struct, '', 'Z')
    raises(TypeError, _struct.Struct, '', 'Z', 'Z')
    raises(TypeError, _struct.Struct, '', 'Z', 'Z', 'Z')
    raises(TypeError, _struct.Struct, '', 'Z', 'Z', 'Z', 'Z')
    raises(TypeError, _struct.Struct, '', 'Z', 'Z', 'Z', 'Z', 'Z')
    raises(TypeError, _struct.Struct, '', 'Z', 'Z', 'Z', 'Z', 'Z', 'Z')
    raises(TypeError, _struct.Struct, '', 'Z', 'Z', 'Z', 'Z', 'Z', 'Z', 'Z')
    raises(TypeError, _struct.Struct, '', 'Z', 'Z', 'Z', 'Z', 'Z', 'Z', 'Z', 'Z')
