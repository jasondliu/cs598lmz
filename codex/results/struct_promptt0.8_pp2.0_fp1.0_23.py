import _struct
# Test _struct.Struct().


def test_unpack():
    s = _struct.Struct('i')
    buf = s.pack(10)
    assert s.size == 4
    assert len(buf) == 4
    assert s.unpack(buf) == (10,)


def test_unpack_from():
    s = _struct.Struct('i')
    buf = s.pack(10)
    assert s.unpack_from(memoryview(buf), 0) == (10,)


def test_struct_simple():
    s = _struct.Struct('i')
    buf = s.pack(10)
    assert len(buf) == s.size
    assert s.unpack(buf) == (10,)


def test_calcsize():
    assert _struct.calcsize('i') == 4


def test_pack():
    assert _struct.pack('i', 10) == b'\n\x00\x00\x00'


def test_unpack_from_endianness():
    s = _struct.Struct('>i')
    buf = s
