import _struct
# Test _struct.Struct

def test_struct_1():
    f = _struct.Struct('i')
    assert f.size == 4
    assert f.pack(1) == b'\x01\x00\x00\x00'
    assert f.unpack(b'\x01\x00\x00\x00') == (1,)
    assert f.unpack_from(b'\x01\x00\x00\x00') == (1,)
    assert f.unpack_from(b'\x01\x00\x00\x00', 1) == ()
    assert f.unpack_from(b'\x01\x00\x00\x00', 0, 1) == (1,)
    assert f.unpack_from(b'\x01\x00\x00\x00', 0, 2) == (1,)
    assert f.unpack_from(b'\x01\x00\x00\x00', 0, 3) == (1,)
