import _struct
# Test _struct.Struct
# XXX: This test is incomplete

def test_struct():
    import struct
    from binascii import hexlify

    s = struct.Struct("i")
    assert s.size == 4
    assert s.pack(1) == b"\x01\x00\x00\x00"
    assert s.unpack(b"\x01\x00\x00\x00") == (1,)
    assert s.unpack_from(b"\x01\x00\x00\x00", 0) == (1,)
    assert s.unpack_from(b"\x01\x00\x00\x00", 0, 1) == (1,)
    assert s.pack_into(b"12345678", 0, 1) == None
    assert hexlify(b"12345678") == b"3132333435363738"
    assert s.pack_into(b"12345678", 1, 1) == None
    assert hexlify(b"12345678") == b"3132333435363738"
   
