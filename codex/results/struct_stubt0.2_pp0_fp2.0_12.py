from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack(b'\x01\x00\x00\x00')

# struct.Struct.__new__(format)
# struct.Struct.__init__(format)
# struct.Struct.unpack(buffer)
# struct.Struct.pack(v1, v2, ...)

# struct.Struct.format
# struct.Struct.size

# struct.pack(format, v1, v2, ...)
# struct.unpack(format, buffer)
# struct.calcsize(format)

# struct.error

# struct.pack_into(format, buffer, offset, v1, v2, ...)
# struct.unpack_from(format, buffer, offset=0)

# struct.iter_unpack(format, buffer)

# struct.pack(format, v1, v2, ...)
# struct.unpack(format, buffer)
# struct.calcsize(format)

# struct.error

# struct.pack_into(format, buffer, offset, v
