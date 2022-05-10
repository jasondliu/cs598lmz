import _struct
# Test _struct.Struct().
def test_struct_struct():
    s = _struct.Struct('cbhilfd')
    assert s.format == 'cbhilfd'
    assert s.size == 1 + 1 + 2 + 4 + 4 + 4 + 8
    # Test alignment
    s = _struct.Struct('@ii')
    assert s.format == 'ii'
    assert s.size == 8
    s = _struct.Struct('=ii')
    assert s.format == 'ii'
    assert s.size == 8
    s = _struct.Struct('<ii')
    assert s.format == 'ii'
    assert s.size == 8
    s = _struct.Struct('>ii')
    assert s.format == 'ii'
    assert s.size == 8
    # Check errors
    py.test.raises(TypeError, _struct.Struct)
    py.test.raises(TypeError, _struct.Struct, None)
    py.test.raises(TypeError, _struct.Struct, '')
    py.test.raises(TypeError, _struct.
