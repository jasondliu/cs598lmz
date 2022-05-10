from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<h')
s.pack(1)

# struct.Struct.__new__(format)
# struct.Struct.__init__(format)
# struct.Struct.pack(v1, v2, ...)
# struct.Struct.unpack(buffer)
# struct.Struct.iter_unpack(buffer)
# struct.Struct.size
# struct.Struct.format
# struct.Struct.pack_into(buffer, offset, v1, v2, ...)
# struct.Struct.unpack_from(buffer, offset=0)
# struct.Struct.iter_unpack_from(buffer, offset=0)

# struct.calcsize(fmt)

# struct.pack(fmt, v1, v2, ...)
# struct.pack_into(fmt, buffer, offset, v1, v2, ...)
# struct.unpack(fmt, buffer)
# struct.unpack_from(fmt, buffer, offset=0)

# struct.error

# struct.Struct.__doc__
#
