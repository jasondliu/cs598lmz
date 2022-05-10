from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# struct.Struct.__new__(struct.Struct, format)
# struct.Struct.__init__(self, format)
# struct.Struct.pack(v1, v2, ...)
# struct.Struct.unpack(buffer)
# struct.Struct.iter_unpack(buffer)
# struct.Struct.size
# struct.Struct.format
# struct.Struct.format_char
# struct.Struct.format_length
# struct.Struct.format_type
# struct.Struct.format_token
# struct.Struct.format_token_is_start
# struct.Struct.format_token_is_size
# struct.Struct.format_token_is_end
# struct.Struct.format_token_is_pad
# struct.Struct.format_token_is_float
# struct.Struct.format_token_is_integer
# struct.Struct.format_token_is_native
# struct.Struct.format_token_is_standard
# struct.Struct.format_token_is_char

