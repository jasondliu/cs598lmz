from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<2i'
s.size = 8
s.pack(1, 2)

# _struct.Struct.__new__()
# _struct.Struct.__new__(format)

# _struct.Struct.format
# _struct.Struct.size
# _struct.Struct.pack(v1, v2, ...)
# _struct.Struct.unpack(buffer)
# _struct.Struct.iter_unpack(buffer)

# _struct.calcsize(format)
# _struct.pack(format, v1, v2, ...)
# _struct.pack_into(format, buffer, offset, v1, v2, ...)
# _struct.unpack(format, buffer)
# _struct.unpack_from(format, buffer, offset=0)
# _struct.iter_unpack(format, buffer)

# _struct.Struct.__doc__
# _struct.Struct.format
# _struct.Struct.size
# _struct.Struct.pack
# _struct.Struct.unpack
# _struct.
