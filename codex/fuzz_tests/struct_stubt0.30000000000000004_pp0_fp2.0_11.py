from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# struct.Struct.__new__(format)
# struct.Struct.__init__(format)
# struct.Struct.pack(v1, v2, ...)
# struct.Struct.unpack(buffer)
# struct.Struct.iter_unpack(buffer)
# struct.Struct.size
# struct.Struct.format
# struct.Struct.format_char
# struct.Struct.format_description
# struct.Struct.pack_into(buffer, offset, v1, v2, ...)
# struct.Struct.unpack_from(buffer, offset=0)
# struct.Struct.iter_unpack_from(buffer, offset=0)
# struct.Struct.unpack(buffer)
# struct.Struct.iter_unpack(buffer)
# struct.Struct.pack_into(buffer, offset, v1, v2, ...)
# struct.Struct.unpack_from(buffer, offset=0)
# struct.Struct.iter_unpack_from(buffer, offset=0)


