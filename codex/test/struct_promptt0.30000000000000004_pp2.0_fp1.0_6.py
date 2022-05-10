import _struct
# Test _struct.Struct

# Test _struct.Struct.format
def test_struct_format():
    assert _struct.Struct('i').format == 'i'
    assert _struct.Struct('ii').format == 'ii'
    assert _struct.Struct('ii').format == 'ii'
    assert _struct.Struct('ii').format == 'ii'
    assert _struct.Struct('ii').format == 'ii'
    assert _struct.Struct('ii').format == 'ii'
    assert _struct.Struct('ii').format == 'ii'
    assert _struct.Struct('ii').format == 'ii'
    assert _struct.Struct('ii').format == 'ii'
    assert _struct.Struct('ii').format == 'ii'
    assert _struct.Struct('ii').format == 'ii'
    assert _struct.Struct('ii').format == 'ii'
    assert _struct.Struct('ii').format == 'ii'
    assert _struct.Struct('ii').format == 'ii'
    assert _struct.Struct('ii').format == 'ii'
