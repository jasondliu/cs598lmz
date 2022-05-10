from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'hhl'
s.size = 8
s.pack(1, 2, 3)

# note that this is a string, not a tuple

# Struct.pack_into(s, buffer, offset, v1, v2, v3)

# Struct.unpack(s, buffer)
# Struct.unpack_from(s, buffer, offset=0)

# Struct()

# s.unpack(b'\x01\x02\x00\x00\x00\x03\x00\x00')

# s.unpack_from(b'\x01\x02\x00\x00\x00\x03\x00\x00', offset=2)

# s.unpack_from(b'\x01\x02\x00\x00\x00\x03\x00\x00', offset=4)

# s.iter_unpack(b'\x01\x02\x00\x00\x00\x03\x00\x00')

# for
