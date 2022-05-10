import _struct
# Test _struct.Struct

def test_struct_unpack():
    s = _struct.Struct('i')
    assert s.unpack(s.pack(42)) == (42,)

def test_struct_unpack_from():
    s = _struct.Struct('i')
    assert s.unpack_from(s.pack(42), 0) == (42,)

def test_struct_unpack_from_offset():
    s = _struct.Struct('ii')
    assert s.unpack_from(s.pack(41, 42), 4) == (42,)

def test_struct_pack_into():
    s = _struct.Struct('i')
    buf = bytearray(s.size)
    s.pack_into(buf, 0, 42)
    assert s.unpack_from(buf, 0) == (42,)

def test_struct_pack_into_offset():
    s = _struct.Struct('ii')
    buf = bytearray(s.size * 2)
    s.pack_into(buf, 4, 42)
    assert
