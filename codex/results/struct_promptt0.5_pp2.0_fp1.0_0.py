import _struct
# Test _struct.Struct.
s = _struct.Struct('l')
s.size
s.pack(1)
s.unpack(s.pack(1))
s.unpack_from(s.pack(1), 0)
s.unpack_from(s.pack(1), 1)
# Test _struct.Struct.iter_unpack.
list(s.iter_unpack(s.pack(1)))
list(s.iter_unpack(s.pack(1), 1))
list(s.iter_unpack(s.pack(1), 2))
list(s.iter_unpack(s.pack(1), 3))
list(s.iter_unpack(s.pack(1), 4))
list(s.iter_unpack(s.pack(1), 5))
# Test _struct.Struct.unpack_from.
s.unpack_from(s.pack(1), 0)
s.unpack_from(s.pack(1), 1)
s.unpack_from(s.pack(1), 2)
s.unpack_from(s.
