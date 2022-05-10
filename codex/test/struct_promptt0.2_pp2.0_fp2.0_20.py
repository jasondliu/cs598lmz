import _struct
# Test _struct.Struct

def test_struct_format_size():
    assert _struct.Struct('i').size == 4
    assert _struct.Struct('ii').size == 8
    assert _struct.Struct('iii').size == 12
    assert _struct.Struct('iiii').size == 16
    assert _struct.Struct('iiiii').size == 20
    assert _struct.Struct('iiiiii').size == 24
    assert _struct.Struct('iiiiiii').size == 28
    assert _struct.Struct('iiiiiiii').size == 32

def test_struct_format_pack():
    assert _struct.Struct('i').pack(1) == b'\x01\x00\x00\x00'
    assert _struct.Struct('ii').pack(1, 2) == b'\x01\x00\x00\x00\x02\x00\x00\x00'
