import _struct
# Test _struct.Struct

def test_struct_int():
    s = _struct.Struct('i')
    assert s.size == 4
    assert s.pack(0) == b'\0\0\0\0'
    assert s.pack(1) == b'\1\0\0\0'
    assert s.pack(-1) == b'\xff\xff\xff\xff'
    assert s.pack(0x12345678) == b'\x78\x56\x34\x12'
    assert s.pack(-0x12345678) == b'\x88\xca\xcb\xed'
    assert s.unpack(b'\0\0\0\0') == (0,)
    assert s.unpack(b'\1\0\0\0') == (1,)
    assert s.unpack(b'\xff\xff\xff\xff') == (-1,)
    assert s.unpack(b'\x78\x56\x34\x12') == (0x12345678,)
    assert s.unpack
