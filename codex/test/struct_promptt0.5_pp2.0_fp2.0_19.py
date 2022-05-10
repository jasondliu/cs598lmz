import _struct
# Test _struct.Struct

def test_struct_simple():
    s = _struct.Struct("i")
    assert s.size == 4
    assert s.pack(1) == b'\x01\x00\x00\x00'
    assert s.unpack(b'\x01\x00\x00\x00') == (1,)
    assert s.unpack_from(b'\x01\x00\x00\x00') == (1,)
    assert s.unpack_from(b'\x01\x00\x00\x00', 0) == (1,)
    assert s.unpack_from(b'\x01\x00\x00\x00', 0, 1) == (1,)
    assert s.pack_into(b'x'*4, 0, 1) == None

def test_struct_format():
    s = _struct.Struct("iii")
    assert s.size == 12
