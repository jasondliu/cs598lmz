import _struct
# Test _struct.Struct

def test_struct_unpack():
    s = _struct.Struct("i")
    assert s.unpack(b"\0\0\0\0") == (0,)
    assert s.unpack(b"\0\0\0\1") == (1,)
    assert s.unpack(b"\0\0\0\xFF") == (255,)
    assert s.unpack(b"\0\0\1\0") == (256,)
    assert s.unpack(b"\0\0\xFF\xFF") == (65535,)
    assert s.unpack(b"\0\1\0\0") == (65536,)
    assert s.unpack(b"\xFF\xFF\xFF\xFF") == (-1,)
    assert s.unpack(b"\xFF\xFF\xFF\xFE") == (-2,)
    assert s.unpack(b"\xFF\xFF\xFF\x00") == (-256,)
