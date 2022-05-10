import _struct
# Test _struct.Struct

def test_struct_pack_unpack():
    s = _struct.Struct('i')
    assert s.size == 4
    assert s.pack(42) == b'*\x00\x00\x00'
    assert s.unpack(b'*\x00\x00\x00') == (42,)

def test_struct_pack_unpack_format():
    s = _struct.Struct('i')
    assert s.pack_into(b'\x00'*4, 0, 42) == None
    assert s.unpack_from(b'*\x00\x00\x00', 0) == (42,)

def test_struct_iter_unpack():
    s = _struct.Struct('ii')
    assert s.size == 8
    assert tuple(s.iter_unpack(b'\x00\x00\x00*\x00\x00\x00+')) == ((42, 43),)

def test_struct_iter_unpack_format():
    s = _struct.Struct('ii')
