import _struct
# Test _struct.Struct

def test_Struct():
    # Basic operations
    s = _struct.Struct("")
    assert s.size == 0
    assert s.pack("") == b""
    assert s.unpack(b"") == ()
    assert s.unpack_from(b"") == ()
    assert s.unpack_from(b"", 0) == ()
    assert s.unpack_from(b"", 0, 0) == ()

    s = _struct.Struct("i")
    assert s.size == struct.calcsize("i")
    assert s.pack(1) == struct.pack("i", 1)
    assert s.unpack(b"\x00\x00\x00\x01") == (1,)
    assert s.unpack_from(b"\x00\x00\x00\x01") == (1,)
    assert s.unpack_from(b"\x00\x00\x00\x01", 0) == (1,)
