import _struct
# Test _struct.Struct
St = _struct.Struct

def test_Struct():
    # simple test
    s = St('i')
    dcs = s.format
    assert dcs == 'i'
    assert s.size == 4
    assert s.pack(12345) == '\x39\x30\x00\x00'
    assert s.unpack('\x39\x30\x00\x00') == (12345,)
    assert s.unpack_from('\x00\x00\x39\x30') == (12345,)

    # test that we can call a Struct multiple times
    s = St('i')
    assert s.size == 4
    assert s.size == 4
    assert s.pack(1234) == '\xD2\x04\x00\x00'
    assert s.pack(4321) == '\x39\x10\x00\x00'
    assert s.unpack_from('\x00\x00\x39\x10') == (4321,)
