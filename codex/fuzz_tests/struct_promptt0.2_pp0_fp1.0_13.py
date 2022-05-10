import _struct
# Test _struct.Struct

def test_struct_error():
    # Issue #15360: _struct.Struct() should raise TypeError if the format
    # string is not a string.
    with pytest.raises(TypeError):
        _struct.Struct(None)

def test_struct_unpack():
    # Issue #15360: _struct.Struct.unpack() should raise TypeError if the
    # format string is not a string.
    with pytest.raises(TypeError):
        _struct.Struct(None).unpack(b'')

def test_struct_pack():
    # Issue #15360: _struct.Struct.pack() should raise TypeError if the
    # format string is not a string.
    with pytest.raises(TypeError):
        _struct.Struct(None).pack(b'')

def test_struct_pack_into():
    # Issue #15360: _struct.Struct.pack_into() should raise TypeError if the
    # format string is not a string.
    with pytest.raises(TypeError):
        _struct.Struct
