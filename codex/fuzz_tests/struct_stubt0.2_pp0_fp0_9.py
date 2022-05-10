from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack(b'\x01\x00\x00\x00')

# struct.Struct.__new__(format)
# struct.Struct.__init__(format)
# struct.Struct.pack(v1, v2, ...)
# struct.Struct.unpack(buffer)
# struct.Struct.iter_unpack(buffer)
# struct.Struct.size
# struct.Struct.format
# struct.Struct.format_char
# struct.Struct.format_re
# struct.Struct.format_parser
# struct.Struct.format_field_types
# struct.Struct.format_field_offsets
# struct.Struct.format_field_names
# struct.Struct.format_field_types_and_offsets
# struct.Struct.format_fields
# struct.Struct.format_check
# struct.Struct.pack_into(buffer, offset, v1, v2, ...)
# struct.Struct.unpack_from(buffer, offset=0)
# struct.Struct.iter_unpack_from
