import _struct
# Test _struct.Struct

def test_struct_error():
    # Issue #17076: check that Struct.__init__() raises a TypeError
    # if the format string is not a string.
    with pytest.raises(TypeError):
        _struct.Struct(None)

def test_struct_unpack():
    # Issue #17076: check that Struct.unpack() raises a TypeError
    # if the buffer is not a string.
    s = _struct.Struct('i')
    with pytest.raises(TypeError):
        s.unpack(None)

def test_struct_unpack_from():
    # Issue #17076: check that Struct.unpack_from() raises a TypeError
    # if the buffer is not a string.
    s = _struct.Struct('i')
    with pytest.raises(TypeError):
        s.unpack_from(None)

def test_struct_pack():
    # Issue #17076: check that Struct.pack() raises a TypeError
    # if the buffer is not a string.
   
