import _struct
# Test _struct.Struct
s = _struct.Struct('i')
s.size
s.pack(42)
s.unpack(_struct.pack('i', 42))

# Test _struct.calcsize
_struct.calcsize('i')

# Test _struct.pack
_struct.pack('i', 42)

# Test _struct.pack_into
buf = bytearray(4)
_struct.pack_into('i', buf, 0, 42)

# Test _struct.unpack
_struct.unpack('i', _struct.pack('i', 42))

# Test _struct.unpack_from
_struct.unpack_from('i', _struct.pack('i', 42))
