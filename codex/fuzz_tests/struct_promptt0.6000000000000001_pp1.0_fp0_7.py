import _struct
# Test _struct.Struct

def test_basic():
    s = _struct.Struct('i')
    data = s.pack(1)
    assert len(data) == 4
    assert s.unpack(data) == (1,)

def test_format():
    s = _struct.Struct('i')
    assert s.format == 'i'
    assert s.size == 4
    assert s.alignment == 4

def test_unpack_from():
    s = _struct.Struct('i')
    data = s.pack(1) + s.pack(2)
    assert s.unpack_from(data) == (1,)
    assert s.unpack_from(data, 4) == (2,)

def test_pack_into():
    s = _struct.Struct('i')
    data = bytearray(8)
    s.pack_into(data, 0, 1)
    s.pack_into(data, 4, 2)
    assert bytes(data) == s.pack(1) + s.pack(2)

def test_iter_un
