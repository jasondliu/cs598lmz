import _struct
# Test _struct.Struct

# Test _struct.Struct.format
s = _struct.Struct('hhl')
assert s.format == 'hhl'

# Test _struct.Struct.size
assert s.size == _struct.calcsize('hhl')

# Test _struct.Struct.pack
assert s.pack(1, 2, 3) == b'\x01\x00\x02\x00\x00\x00\x00\x00\x03\x00\x00\x00'

# Test _struct.Struct.unpack
assert s.unpack(b'\x01\x00\x02\x00\x00\x00\x00\x00\x03\x00\x00\x00') == (1, 2, 3)

# Test _struct.Struct.iter_unpack
