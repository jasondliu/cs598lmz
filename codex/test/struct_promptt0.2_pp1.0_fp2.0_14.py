import _struct
# Test _struct.Struct

def test_struct_pack():
    s = _struct.Struct('i')
    assert s.pack(1) == b'\x01\x00\x00\x00'
    assert s.pack(1, 2) == b'\x01\x00\x00\x00'
    assert s.pack(1, 2, 3) == b'\x01\x00\x00\x00'
    assert s.pack(1, 2, 3, 4) == b'\x01\x00\x00\x00'
    assert s.pack(1, 2, 3, 4, 5) == b'\x01\x00\x00\x00'
    assert s.pack(1, 2, 3, 4, 5, 6) == b'\x01\x00\x00\x00'
    assert s.pack(1, 2, 3, 4, 5, 6, 7) == b'\x01\x00\x00\x00'
