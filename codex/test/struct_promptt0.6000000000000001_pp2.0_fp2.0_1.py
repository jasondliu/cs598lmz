import _struct
# Test _struct.Struct

def test_Struct():
    import _struct
    for code in 'bBhHiIlLqQfd':
        s = _struct.Struct(code)
        assert s.size == _struct.calcsize(code)
        assert s.format == code
        assert s.pack(0) == _struct.pack(code, 0)
        assert s.unpack(_struct.pack(code, 42)) == (42,)
        assert s.unpack_from(_struct.pack(code, 42)) == (42,)
        assert s.unpack_from(_struct.pack(code, 42), 1) == ()

    s = _struct.Struct('12s')
    assert s.unpack(b'x' * 12) == (b'x' * 12,)
    assert s.unpack_from(b'x' * 12, 0) == (b'x' * 12,)
    assert s.unpack_from(b'x' * 12, 1) == (b'x' * 11,)
