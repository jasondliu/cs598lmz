import _struct
# Test _struct.Struct.

# test struct packing and unpacking
s = _struct.Struct("i")
buf = s.pack(1)
s.unpack(buf)

# test struct iter unpacking
s = _struct.Struct("iii")
buf = s.pack(1, 2, 3)
list(s.iter_unpack(buf))

# test struct size
s = _struct.Struct("i")
s.size

# test struct alignment
s = _struct.Struct("i")
s.alignment

# test struct format
s = _struct.Struct("i")
s.format

# test struct pack_into
buf = bytearray(s.size * 2)
s.pack_into(buf, 0, 1)
s.pack_into(buf, s.size, 2)

# test struct unpack_from
buf = s.pack(1) + s.pack(2)
s.unpack_from(buf, 0)
s.unpack_from(buf, s.size)

# test struct iter_unpack_from
