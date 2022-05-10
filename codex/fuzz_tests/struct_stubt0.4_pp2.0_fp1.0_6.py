from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

# _struct.Struct.unpack
s.unpack(b'\x00\x00\x00\x00')

# _struct.Struct.unpack_from
s.unpack_from(b'\x00\x00\x00\x00')

# _struct.Struct.pack
s.pack(0)

# _struct.Struct.pack_into
s.pack_into(b'', 0, 0)

# _struct.Struct.iter_unpack
list(s.iter_unpack(b'\x00\x00\x00\x00'))

# _struct.Struct.iter_unpack_from
list(s.iter_unpack_from(b'\x00\x00\x00\x00'))

# _struct.Struct.format
s.format

# _struct.Struct.format_length
s.format_length

# _struct.Struct.size
s.size

# _struct.Struct.alignment

