from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack(b'\x00\x00\x00\x00')

# struct.Struct.__new__(format)
# struct.Struct.__init__(format)
# struct.Struct.unpack(buffer)
# struct.Struct.pack(v1, v2, ...)
# struct.Struct.iter_unpack(buffer)
# struct.Struct.size
# struct.Struct.format
# struct.Struct.format_char
# struct.Struct.format_re
# struct.Struct.format_parser
# struct.Struct.pack_into(buffer, offset, v1, v2, ...)
# struct.Struct.unpack_from(buffer, offset=0)
# struct.Struct.iter_unpack_from(buffer, offset=0)
# struct.Struct.pack(v1, v2, ...)
# struct.Struct.unpack(buffer)
# struct.Struct.iter_unpack(buffer)
# struct.Struct.pack_into(buffer, offset, v1, v2, ...
