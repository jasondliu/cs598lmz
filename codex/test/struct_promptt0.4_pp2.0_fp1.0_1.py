import _struct
# Test _struct.Struct.

def test_struct(fmt, expected):
    s = _struct.Struct(fmt)
    got = s.pack(*expected)
    assert s.unpack(got) == expected
    assert s.size == len(got)

# Test _struct.Struct with standard format characters.

# Standard size and alignment tests
test_struct('xcbhHiIlLqQfdspP',
            (b'\x00', b'A', b'\x01',
             0x0102, 0x01020304, 0x010203040506, 0x0102030405060708,
             0x0102030405060708, 0x0102030405060708, 0x0102030405060708,
             0.0, 1.0, 1.0, b'', b'12345678'))

# Native size and alignment tests
