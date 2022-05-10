import _struct
# Test _struct.Struct

# test __new__
def test_new_1():
    assert _struct.Struct('i')
    raises(ValueError, _struct.Struct, 'z')
    raises(ValueError, _struct.Struct, 'P')
    raises(TypeError, _struct.Struct, 'ii')
    raises(TypeError, _struct.Struct, 'c')
    raises(TypeError, _struct.Struct, 'cc')
    raises(TypeError, _struct.Struct, 'ccc')
    raises(TypeError, _struct.Struct, 'cccc')
    raises(TypeError, _struct.Struct, 'ccccc')
    raises(TypeError, _struct.Struct, 'cccccc')
    raises(TypeError, _struct.Struct, 'ccccccc')
    raises(TypeError, _struct.Struct, 'cccccccc')
    raises(TypeError, _struct.Struct, 'ccccccccc')
    raises(TypeError, _struct.Struct, 'cccccccccc')
    raises(TypeError, _struct.Struct, 'cccccc
