import _struct
# Test _struct.Struct

def test_struct_error():
    with pytest.raises(TypeError):
        _struct.Struct()
    with pytest.raises(TypeError):
        _struct.Struct('', '>')
    with pytest.raises(TypeError):
        _struct.Struct('', '>', 0)
    with pytest.raises(TypeError):
        _struct.Struct('', '>', 0, 0)
    with pytest.raises(TypeError):
        _struct.Struct('', '>', 0, 0, 0)

def test_struct_unpack():
    s = _struct.Struct('i')
    assert s.unpack(b'abcd') == (1684234849,)
    assert s.unpack(b'abcd', 2) == (1633837924,)
    assert s.unpack(b'abcdef', 2) == (1633837924,)
    assert s.unpack(b'abcdef', 2, 2) == (1684234849,)
