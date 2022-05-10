import _struct
# Test _struct.Struct
s = _struct.Struct('i')
s2 = _struct.Struct('ii')
s3 = _struct.Struct('iii')

def test_struct_pack(s, s2, s3):

    # Test packing
    assert s.pack(-1) == b'\x01\x00\x00\x00'
    assert s.pack(10) == b'\n\x00\x00\x00'
    assert s.pack(2**32-1) == b'\xff\xff\xff\xff'
    assert s.pack(2**31-1) == b'\xff\xff\xff\x7f'
    assert s.pack(2**31) == b'\x00\x00\x00\x80'
    assert s.pack(2**63-1) == b'\xff\xff\xff\xff\xff\xff\xff\x7f'
    assert s.pack(2**63) == b'\x00\x00\x00\x00\x00\x00\x00\x80'
