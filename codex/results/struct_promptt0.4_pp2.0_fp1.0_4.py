import _struct
# Test _struct.Struct()

# Test the basic functionality

def test_basic():
    # Initialize
    s = _struct.Struct('i')
    assert s.size == 4
    assert s.format == 'i'
    assert s.pack(0x12345678) == b'\x12\x34\x56\x78'
    assert s.unpack(b'\x12\x34\x56\x78') == (0x12345678,)
    assert s.unpack_from(b'\x12\x34\x56\x78', 0) == (0x12345678,)
    assert s.unpack_from(b'\x00\x12\x34\x56\x78', 1) == (0x12345678,)
    assert s.unpack_from(b'\x00\x12\x34\x56\x78', 1, 2) == (0x345678,)
    assert s.pack_into(b'\x00'*4, 1, 0x12345678) == None
    assert b'\x
