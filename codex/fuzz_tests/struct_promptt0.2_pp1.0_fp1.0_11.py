import _struct
# Test _struct.Struct

def test_struct_error():
    # Issue #17093: _struct.Struct() should raise a TypeError if the format
    # string is not a string.
    with pytest.raises(TypeError):
        _struct.Struct(None)
    with pytest.raises(TypeError):
        _struct.Struct(42)
    with pytest.raises(TypeError):
        _struct.Struct(b"b")

def test_struct_unpack():
    # Issue #17093: _struct.Struct.unpack() should raise a TypeError if the
    # buffer is not a string.
    s = _struct.Struct("b")
    with pytest.raises(TypeError):
        s.unpack(None)
    with pytest.raises(TypeError):
        s.unpack(42)
    with pytest.raises(TypeError):
        s.unpack(b"b")

def test_struct_unpack_from():
    # Issue #17093: _struct.Struct.unpack_from() should
