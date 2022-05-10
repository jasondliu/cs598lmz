import _struct
# Test _struct.Struct with the native byte order

def test_native():
    s = _struct.Struct("hil")
    assert s.size == 12
    assert s.format == "hil"
    assert s.unpack(b"\x01\x00\x00\x00\x02\x00\x00\x00"
                    b"\x03\x00\x00\x00") == (1, 2, 3)
    assert s.pack(1, 2, 3) == b"\x01\x00\x00\x00\x02\x00\x00\x00" \
                              b"\x03\x00\x00\x00"
    raises(struct.error, s.unpack, b"\x01\x00\x00\x00\x02\x00\x00\x00"
                                  b"\x03\x00")
    raises(struct.error, s.pack, 1, 2, 3, 4)

def test_little():
    s = _struct.Struct("<hil")

