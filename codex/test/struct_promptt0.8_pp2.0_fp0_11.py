import _struct
# Test _struct.Struct methods

# Test the 'size' method:
for fmt in (b'', b'xxxx'):
    s = _struct.Struct(fmt)
    assert s.size == len(fmt), fmt
    # Test with explicit size:
    s2 = _struct.Struct(fmt, 42)
    assert s2.size == 42, fmt

# Test the 'format' method:
for fmt in (b'', b'xxxx'):
    s = _struct.Struct(fmt)
    assert s.format == fmt, fmt
    # Test with explicit size:
    s2 = _struct.Struct(fmt, 42)
    assert s2.format == fmt, fmt

# Test the 'pack' method:
for fmt in (b'i', b'ii', b'b', b'hhhhh'):
    s = _struct.Struct(fmt)
    assert s.pack(*range(s.size)) == _struct.pack(fmt, *range(s.size)), fmt

# Test the 'pack_into' method:
