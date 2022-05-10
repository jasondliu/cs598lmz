import _struct
# Test _struct.Struct
_struct.Struct('i').pack(1)

# Test _struct.error
_struct.error

# Test _struct.calcsize
_struct.calcsize('i')

# Test _struct.pack
_struct.pack('i', 1)

# Test _struct.unpack
_struct.unpack('i', _struct.pack('i', 1))

# Test _struct.iter_unpack
list(_struct.iter_unpack('i', _struct.pack('i', 1)))

# Test _struct.pack_into
buf = bytearray(4)
_struct.pack_into('i', buf, 0, 1)

# Test _struct.unpack_from
_struct.unpack_from('i', buf, 0)

# Test _struct.iter_unpack_from
list(_struct.iter_unpack_from('i', buf, 0))

# Test _struct.Struct.__init__
s = _struct.Struct('i')
s.size
s.format

# Test _struct.Struct.pack

