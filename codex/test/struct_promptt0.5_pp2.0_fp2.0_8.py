import _struct
# Test _struct.Struct('i')

def test_struct_i():
    s = _struct.Struct('i')
    assert s.size == 4
    assert s.pack(0) == b'\x00\x00\x00\x00'
    assert s.pack(1) == b'\x01\x00\x00\x00'
    assert s.pack(-1) == b'\xff\xff\xff\xff'
    assert s.pack(2**31-1) == b'\xff\xff\xff\x7f'
    assert s.pack(-2**31) == b'\x00\x00\x00\x80'
    assert s.unpack(b'\x00\x00\x00\x00') == (0,)
    assert s.unpack(b'\x01\x00\x00\x00') == (1,)
    assert s.unpack(b'\xff\xff\xff\xff') == (-1,)
