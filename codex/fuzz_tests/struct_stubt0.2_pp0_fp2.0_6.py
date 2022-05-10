from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.unpack(b'\x00\x00\x00\x00')

# _struct.Struct.__new__(format)
# _struct.Struct.__init__(format)
# _struct.Struct.unpack(buffer)
# _struct.Struct.pack(v1, v2, ...)

# struct.pack(format, v1, v2, ...)
# struct.unpack(format, buffer)
# struct.calcsize(format)

# struct.Struct(format)

# struct.pack_into(format, buffer, offset, v1, v2, ...)
# struct.unpack_from(format, buffer, offset=0)

# struct.iter_unpack(format, buffer)
# struct.iter_unpack(format, buffer, offset=0)

# struct.pack(format, v1, v2, ...)
# struct.unpack(format, buffer)
# struct.calcsize(format)

# struct.Struct(format)

#
