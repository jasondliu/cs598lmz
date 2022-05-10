import _struct
# Test _struct.Struct

def test_struct_unpack():
    s = _struct.Struct("i")
    assert s.unpack(b"\0\0\0\0") == (0,)
    assert s.unpack(b"\0\0\0\1") == (1,)
    assert s.unpack(b"\0\0\0\2") == (2,)
    assert s.unpack(b"\0\0\0\3") == (3,)
    assert s.unpack(b"\0\0\0\4") == (4,)
    assert s.unpack(b"\0\0\0\5") == (5,)
    assert s.unpack(b"\0\0\0\6") == (6,)
    assert s.unpack(b"\0\0\0\7") == (7,)
    assert s.unpack(b"\0\0\0\10") == (8,)
    assert s.unpack(b"\0\0\0\11") == (9,)
    assert s.
