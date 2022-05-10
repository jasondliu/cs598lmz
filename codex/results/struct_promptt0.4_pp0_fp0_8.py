import _struct
# Test _struct.Struct.
s = _struct.Struct('i')
s.size
s.pack(1)
s.unpack(s.pack(1))
s.unpack_from(s.pack(1), 0)
s.unpack_from(s.pack(1), 1)

# Test _struct.pack.
_struct.pack('i', 1)
_struct.pack('i', 1, 2)
_struct.pack('i', 1, 2, 3)
_struct.pack('i', 1, 2, 3, 4)

# Test _struct.unpack.
_struct.unpack('i', _struct.pack('i', 1))
_struct.unpack('i', _struct.pack('i', 1), 1)
_struct.unpack('i', _struct.pack('i', 1), 1, 2)

# Test _struct.calcsize.
_struct.calcsize('i')
_struct.calcsize('i', 1)
_struct.calcsize('i', 1, 2)
