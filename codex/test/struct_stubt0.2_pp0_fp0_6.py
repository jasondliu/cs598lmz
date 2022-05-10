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
# struct.Struct.format_re
# struct.Struct.format_parser
# struct.Struct.format_field_char
# struct.Struct.format_field_name
# struct.Struct.format_field_types
# struct.Struct.format_field_type
# struct.Struct.format_field_size
# struct.Struct.format_field_offset
# struct.Struct.format_field_struct
# struct.Struct.format_field_struct_char
# struct.Struct.format_field_struct_type
# struct.Struct.format_field_struct_format
# struct.Struct.format_field_struct_names
# struct.
