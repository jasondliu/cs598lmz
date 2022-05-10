from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# struct.Struct.pack(format, v1, v2, ...)
# struct.Struct.unpack(buffer)

# struct.pack_into(format, buffer, offset, v1, v2, ...)
# struct.unpack_from(format, buffer, offset=0)

# struct.calcsize(format)

# struct.error

# struct.pack(format, v1, v2, ...)
# struct.unpack(format, buffer)

# struct.iter_unpack(format, buffer)

# struct.Struct(format)

# struct.Struct.__new__(format)

# struct.Struct.__init__(format)

# struct.Struct.pack(v1, v2, ...)

# struct.Struct.unpack(buffer)

# struct.Struct.pack_into(buffer, offset, v1, v2, ...)

# struct.Struct.unpack_from(buffer, offset=0)

# struct.
