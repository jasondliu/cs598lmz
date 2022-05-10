import _struct
# Test _struct.Struct.unpack()

def test_unpack():
    s = _struct.Struct('i')
    assert s.unpack(s.pack(1)) == (1,)
    assert s.unpack(s.pack(0)) == (0,)
    assert s.unpack(s.pack(-1)) == (-1,)
    assert s.unpack(s.pack(2**31-1)) == (2**31-1,)
    assert s.unpack(s.pack(-2**31)) == (-2**31,)
    assert s.unpack(s.pack(-2**31+1)) == (-2**31+1,)
    assert s.unpack(s.pack(2**31)) == (2**31,)
    assert s.unpack(s.pack(2**31-1)) == (2**31-1,)
    assert s.unpack(s.pack(-2**31)) == (-2**31,)
    assert s.unpack(s.pack(-2**31+1)) == (-2**31+1,)
