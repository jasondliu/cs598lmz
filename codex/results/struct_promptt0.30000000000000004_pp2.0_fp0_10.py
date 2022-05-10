import _struct
# Test _struct.Struct.

def test_struct_pack():
    s = _struct.Struct('i')
    assert s.size == 4
    assert s.pack(1) == b'\x01\x00\x00\x00'
    assert s.pack(1, 2) == b'\x01\x00\x00\x00'
    assert s.pack_into(bytearray(b'xxxx'), 1, 2) == None
    assert bytearray(b'xxxx') == b'\x01\x00\x00\x00'

def test_struct_unpack():
    s = _struct.Struct('i')
    assert s.unpack(b'\x01\x00\x00\x00') == (1,)
    assert s.unpack_from(b'\x01\x00\x00\x00', 0) == (1,)
    assert s.unpack_from(b'xxxx\x01\x00\x00\x00', 4) == (1,)

def test_struct_iter_unpack():
