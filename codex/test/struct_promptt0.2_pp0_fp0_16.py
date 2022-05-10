import _struct
# Test _struct.Struct

# Test _struct.Struct.__new__

# Test _struct.Struct.__new__ with invalid format
try:
    _struct.Struct('Q')
except ValueError:
    pass
else:
    print('Failed to raise ValueError for invalid format')

# Test _struct.Struct.__new__ with valid format
s = _struct.Struct('i')

# Test _struct.Struct.format
assert s.format == 'i'

# Test _struct.Struct.size
assert s.size == _struct.calcsize('i')

# Test _struct.Struct.pack
assert s.pack(1) == _struct.pack('i', 1)

# Test _struct.Struct.pack_into
buf = bytearray(s.size)
s.pack_into(buf, 0, 1)
assert buf == _struct.pack('i', 1)

# Test _struct.Struct.unpack
assert s.unpack(s.pack(1)) == (1,)

# Test _struct.Struct.unpack_from
