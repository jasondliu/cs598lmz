import _struct
# Test _struct.Struct().
# Test with format string and without.
for fmt in [_struct.pack_format(_struct.calcsize('iii')), 'iii']:
    s = _struct.Struct(fmt)
    # Test pack, pack_into, unpack, unpack_from, size.
    b = s.pack(1, 2, 3)
    print(s.unpack(b), b)
    b = bytearray(b"\0" * s.size)
    s.pack_into(b, 0, 1, b'2', 3.0)
    print(s.unpack_from(b, 0), b)
    b = s.pack(1, b'2', 3.0)
    print(s.unpack(b), b)
    b = bytearray(b"\0" * s.size)
    s.pack_into(b, 0, 1, b'2', 3.0)
    print(s.unpack_from(b, 0), b)
    b = s.pack(1, b'2', 3
