import _struct
# Test _struct.Struct


def test_struct():
    s = _struct.Struct('i')
    assert s.size == 4
    assert s.pack(1) == b'\x01\x00\x00\x00'
    assert s.unpack(b'\x01\x00\x00\x00') == (1,)
    assert s.unpack_from(b'\x01\x00\x00\x00') == (1,)
    assert s.calcsize() == 4
    assert s.format == 'i'

    s = _struct.Struct('i3s')
    assert s.size == 8
    assert s.pack(1, b'abc') == b'\x01\x00\x00\x00abc'
    assert s.unpack(b'\x01\x00\x00\x00abc') == (1, b'abc')
    assert s.unpack_from(b'\x01\x00\x00\x00abc') == (1, b'abc')
    assert s.calcsize() == 8
