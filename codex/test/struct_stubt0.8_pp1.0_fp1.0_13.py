from _struct import Struct
s = Struct.__new__(Struct)
s.formatstring = '=hi12s'
s.size = 18
s.alignment = 4
s.formatarg = None

s.pack(10, 20, 'abc')

# s = Struct(format,...)
# s.size
# s.pack(v1, v2, ...)
# s.pack_into(buffer, offset, v1, v2, ...)
# s.unpack_from(buffer[, offset])
# s.unpack(buffer)

s = Struct('=hi12s')
s.size
s.pack(10, 20, 'abc')
s.pack_into(new_buffer, 1, 10, 20, 'abc')
s.unpack_from(buffer, offset)
s.unpack(buffer)

# format string
# byte order: <, >, =
# size: c, b, B, h, H, i, I, l, L, f, d, q, Q, s, p, P
# alignment: x

# c: char
# b, B: signed and unsigned char
