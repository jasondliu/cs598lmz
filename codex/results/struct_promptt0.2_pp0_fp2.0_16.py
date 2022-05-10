import _struct
# Test _struct.Struct

# Test the basic constructors
s = _struct.Struct('i')
s = _struct.Struct('i', _struct.LITTLE_ENDIAN)
s = _struct.Struct('i', _struct.BIG_ENDIAN)
s = _struct.Struct('i', _struct.NATIVE_ENDIAN)
s = _struct.Struct('i', _struct.NETWORK_ENDIAN)

# Test the format string
s = _struct.Struct('i')
assert s.format == 'i'

# Test the size
s = _struct.Struct('i')
assert s.size == 4

# Test the pack/unpack methods
s = _struct.Struct('i')
packed = s.pack(42)
assert s.unpack(packed) == (42,)

# Test the pack_into/unpack_from methods
s = _struct.Struct('i')
buf = bytearray(s.size)
s.pack_into(buf, 0, 42)
assert s.unpack_from(buf, 0) == (42,)

# Test
