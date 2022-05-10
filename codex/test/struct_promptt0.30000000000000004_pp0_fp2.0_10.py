import _struct
# Test _struct.Struct

# Test _struct.Struct

def test_basic():
    with pytest.raises(TypeError):
        _struct.Struct()
    with pytest.raises(TypeError):
        _struct.Struct(42)
    with pytest.raises(TypeError):
        _struct.Struct('')
    with pytest.raises(TypeError):
        _struct.Struct('', 42)

    s = _struct.Struct('i')
    assert s.format == 'i'
    assert s.size == struct.calcsize('i')
    assert s.alignment == struct.calcsize('i')

    s = _struct.Struct('P')
    assert s.format == 'P'
    assert s.size == struct.calcsize('P')
    assert s.alignment == struct.calcsize('P')

    s = _struct.Struct('Pii')
    assert s.format == 'Pii'
    assert s.size == struct.calcsize('Pii')
