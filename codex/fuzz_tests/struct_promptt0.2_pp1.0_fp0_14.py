import _struct
# Test _struct.Struct

def test_struct_pack():
    s = _struct.Struct('i')
    assert s.size == 4
    assert s.pack(1) == b'\x01\x00\x00\x00'
    assert s.pack(1, 2) == b'\x01\x00\x00\x00'
    assert s.pack(1, 2, 3) == b'\x01\x00\x00\x00'
    assert s.pack(1, 2, 3, 4) == b'\x01\x00\x00\x00'
    assert s.pack_into(bytearray(b'xxxx'), 0, 1) == None
    assert s.pack_into(bytearray(b'xxxx'), 1, 1) == None
    assert s.pack_into(bytearray(b'xxxx'), 2, 1) == None
    assert s.pack_into(bytearray(b'xxxx'), 3, 1) == None
    assert s.pack_into(bytearray(b'xxxx'), 4,
