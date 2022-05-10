import _struct
# Test _struct.Struct

# Test pack/unpack
s = _struct.Struct('i')
packed = s.pack(1)
assert s.unpack(packed) == (1,)

# Test pack_into/unpack_from
buf = bytearray(4)
s.pack_into(buf, 0, 1)
assert s.unpack_from(buf, 0) == (1,)

# Test size
assert s.size == 4

# Test format
assert s.format == 'i'

# Test iter
assert list(s) == ['i']

# Test repr
assert repr(s) == "Struct('i')"

# Test new
s = _struct.Struct('i')
assert s.format == 'i'

# Test new with keyword arguments
s = _struct.Struct(format='i')
assert s.format == 'i'

# Test new with unknown keyword argument
