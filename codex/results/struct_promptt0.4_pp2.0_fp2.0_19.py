import _struct
# Test _struct.Struct.
s = _struct.Struct('i')
s.size
s.pack(1)
s.unpack(_struct.pack('i', 1))
s.unpack_from(_struct.pack('ii', 1, 2), 4)

# Test _struct.pack.
_struct.pack('i', 1)
_struct.pack('ii', 1, 2)

# Test _struct.unpack.
_struct.unpack('i', _struct.pack('i', 1))
_struct.unpack('ii', _struct.pack('ii', 1, 2))

# Test _struct.unpack_from.
_struct.unpack_from('i', _struct.pack('ii', 1, 2), 4)
_struct.unpack_from('ii', _struct.pack('iii', 1, 2, 3), 4)

# Test _struct.calcsize.
_struct.calcsize('i')
_struct.calcsize('ii')

# Test _struct.iter_unpack.
list(_struct.iter_unpack('i', _struct.pack
