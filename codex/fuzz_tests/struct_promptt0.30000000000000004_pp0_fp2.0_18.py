import _struct
# Test _struct.Struct

def test_struct_pack():
    assert _struct.Struct('i').pack(1) == b'\x01\x00\x00\x00'
    assert _struct.Struct('i').pack(1, 2) == b'\x01\x00\x00\x00'
    assert _struct.Struct('ii').pack(1, 2) == b'\x01\x00\x00\x00\x02\x00\x00\x00'
    assert _struct.Struct('ii').pack(1) == b'\x01\x00\x00\x00\x00\x00\x00\x00'
    assert _struct.Struct('ii').pack(1, 2, 3) == b'\x01\x00\x00\x00\x02\x00\x00\x00'
    assert _struct.Struct('ii').pack(1, 2, 3, 4) == b'\x01\x00\x00\x00\x02\x00\x00\x00'
    assert _struct
