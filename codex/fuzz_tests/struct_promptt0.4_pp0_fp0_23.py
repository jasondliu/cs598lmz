import _struct
# Test _struct.Struct
s = _struct.Struct('h')
s.size
s.pack(1)
s.pack_into(b'', 0, 1)
s.unpack(b'\x01\x00')
s.unpack_from(b'\x01\x00', 0)

# Test _struct.Struct.from_param
s = _struct.Struct('h')
s.from_param(1)

# Test _struct.calcsize
_struct.calcsize('h')

# Test _struct.pack
_struct.pack('h', 1)

# Test _struct.pack_into
_struct.pack_into(b'', 0, 'h', 1)

# Test _struct.unpack
_struct.unpack('h', b'\x01\x00')

# Test _struct.unpack_from
_struct.unpack_from('h', b'\x01\x00', 0)
