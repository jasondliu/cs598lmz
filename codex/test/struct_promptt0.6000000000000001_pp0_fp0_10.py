import _struct
# Test _struct.Struct.

fmt = 'hhl'
s = _struct.Struct(fmt)

# Check format parsing
for c in s.format:
    if c == 'x':
        assert c in s.format
    else:
        assert c in 'cbBhHiIlLfdsp'

# check format size
assert s.size == _struct.calcsize(fmt)

# check _struct.pack
assert ('\000\000\000\000\000\000\000\001',) == s.unpack(s.pack(1))

# check _struct.pack_into
buf = bytearray(s.size)
s.pack_into(buf, 0, 1)
assert buf == bytearray(s.pack(1))

# check _struct.unpack
assert (1,) == s.unpack(s.pack(1))

# check _struct.unpack_from
buf = bytearray(s.pack(1))
assert (1,) == s.unpack_from(buf, 0)
