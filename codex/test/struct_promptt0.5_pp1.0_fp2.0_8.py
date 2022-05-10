import _struct
# Test _struct.Struct
def test_Struct():
    s = _struct.Struct("i")
    for fmt in ("b", "h", "i", "l", "q"):
        s = _struct.Struct(fmt)
        assert s.size == _struct.calcsize(fmt)
        assert s.format == fmt
        assert s.unpack("\x01\x02\x03\x04")[0] == 0x01020304
        assert s.pack(0x01020304) == "\x01\x02\x03\x04"
        assert s.unpack_from("\x11\x22\x33\x44\x55\x66\x77\x88", 4)[0] == 0x55667788
        assert s.pack_into("\x00" * 8, 4, 0x55667788) == None
        assert s.unpack_from(memoryview("\x11\x22\x33\x44\x55\x66\x77\x88"), 4)[0] == 0x55667788

