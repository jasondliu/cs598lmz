import _struct
# Test _struct.Struct

# Test _struct.Struct.__new__

def test_new():
    # Test _struct.Struct.__new__
    assert _struct.Struct('i').format == 'i'
    assert _struct.Struct('i').size == 4
    assert _struct.Struct('i').__doc__ == 'Compiled struct object'
    raises(TypeError, _struct.Struct, 'i', 'j')
    raises(TypeError, _struct.Struct, 'i', 'j', 'k')
    raises(TypeError, _struct.Struct, 'i', 'j', 'k', 'l')
    raises(TypeError, _struct.Struct, 'i', 'j', 'k', 'l', 'm')
    raises(TypeError, _struct.Struct, 'i', 'j', 'k', 'l', 'm', 'n')
    raises(TypeError, _struct.Struct, 'i', 'j', 'k', 'l', 'm', 'n', 'o')
