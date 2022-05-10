import _struct
# Test _struct.Struct.__repr__
def test_struct_repr():
    s = _struct.Struct('i')
    assert repr(s) == "<class '_struct.Struct'>"


# Test _struct.Struct.format
def test_struct_format():
    s = _struct.Struct('i')
    assert s.format == 'i'


# Test _struct.Struct.size
def test_struct_size():
    s = _struct.Struct('i')
    assert s.size == 4


# Test _struct.Struct.pack
def test_struct_pack():
    s = _struct.Struct('i')
    assert s.pack(1) == b'\x01\x00\x00\x00'
    assert s.pack(1, 2) == b'\x01\x00\x00\x00'


# Test _struct.Struct.unpack
def test_struct_unpack():
    s = _struct.Struct('i')
