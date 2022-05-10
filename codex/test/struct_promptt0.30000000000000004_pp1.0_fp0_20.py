import _struct
# Test _struct.Struct.
s = _struct.Struct("i")
s.size
s.pack(1)
s.unpack(_struct.pack("i", 1))
s.unpack_from(_struct.pack("i", 1), 0)
s.iter_unpack(_struct.pack("i", 1))

# Test _struct.Struct.format.
s = _struct.Struct("i")
s.format

# Test _struct.Struct.unpack_from.
s = _struct.Struct("i")
s.unpack_from(_struct.pack("i", 1), 0)

# Test _struct.Struct.iter_unpack.
s = _struct.Struct("i")
list(s.iter_unpack(_struct.pack("i", 1)))

# Test _struct.Struct.pack_into.
s = _struct.Struct("i")
buf = bytearray(s.size)
s.pack_into(buf, 0, 1)

# Test _struct.Struct.unpack_from.
s = _struct.Struct("i")
buf = byt
