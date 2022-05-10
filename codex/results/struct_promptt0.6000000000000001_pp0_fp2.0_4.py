import _struct
# Test _struct.Struct and _struct.pack_into

def test_struct():
    s = _struct.Struct("hhl")
    assert len(s.pack(1, 2, 3)) == s.size
    assert s.unpack(s.pack(1, 2, 3)) == (1, 2, 3)
    assert s.unpack_from(s.pack(1, 2, 3)) == (1, 2, 3)
    assert s.unpack_from(s.pack(1, 2, 3), 1) == (2, 3, 0)
    assert s.unpack_from(s.pack(1, 2, 3), 1, 2) == (2, 3)
    f = StringIO()
    assert s.pack_into(f, 0, 1, 2, 3) is None
    assert f.getvalue() == s.pack(1, 2, 3)
    assert s.pack_into(f, 0, 1, 2, 3, 4) is None
    assert f.getvalue() == s.pack(1, 2, 3) + "\x04\x00\
