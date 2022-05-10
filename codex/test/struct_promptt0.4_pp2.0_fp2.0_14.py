import _struct
# Test _struct.Struct

def test_struct_pack_unpack():
    s = _struct.Struct('i')
    buf = s.pack(42)
    assert s.unpack(buf) == (42,)

def test_struct_unpack_from():
    s = _struct.Struct('i')
    buf = s.pack(42)
    assert s.unpack_from(buf) == (42,)

def test_struct_unpack_from_buffer():
    s = _struct.Struct('i')
    buf = s.pack(42)
    assert s.unpack_from(buffer(buf)) == (42,)

def test_struct_calcsize():
    s = _struct.Struct('i')
    assert s.size == 4

def test_struct_iter():
    s = _struct.Struct('i')
    assert list(s.iter_unpack(s.pack(42))) == [(42,)]

def test_struct_iter_buffer():
    s = _struct.Struct('i')
