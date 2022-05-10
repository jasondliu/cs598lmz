import _struct
# Test _struct.Struct

def test_struct_iter():
    s = _struct.Struct('3i')
    assert list(s) == [3, 'i']

def test_struct_pack():
    s = _struct.Struct('3i')
    assert s.pack(1, 2, 3) == b'\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00'

def test_struct_unpack():
    s = _struct.Struct('3i')
    assert s.unpack(b'\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00') == (1, 2, 3)

def test_struct_unpack_from():
    s = _struct.Struct('3i')
