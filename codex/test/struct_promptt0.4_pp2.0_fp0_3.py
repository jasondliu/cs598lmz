import _struct
# Test _struct.Struct

# _struct.Struct(fmt)
# fmt: format string

# struct.pack(fmt, v1, v2, ...)
# fmt: format string
# v1, v2, ...: values

# struct.unpack(fmt, string)
# fmt: format string
# string: packed data

# struct.calcsize(fmt)
# fmt: format string

# struct.error

# struct.pack_into(fmt, buffer, offset, v1, v2, ...)
# fmt: format string
# buffer: mutable buffer
# offset: start position
# v1, v2, ...: values

# struct.unpack_from(fmt, buffer, offset=0)
# fmt: format string
# buffer: packed data
# offset: start position

# struct.iter_unpack(fmt, buffer)
# fmt: format string
# buffer: packed data

# struct.Struct.pack(v1, v2, ...)
# v1, v2, ...: values

# struct.Struct.pack_
