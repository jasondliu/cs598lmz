from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i?f')
s.size

# _struct.Struct.__new__(format)
# _struct.Struct.__init__(format)
# _struct.Struct.pack(v1, v2, ...)
# _struct.Struct.pack_into(buffer, offset, v1, v2, ...)
# _struct.Struct.unpack(buffer)
# _struct.Struct.unpack_from(buffer, offset=0)
# _struct.Struct.iter_unpack(buffer)
# _struct.Struct.format
# _struct.Struct.size
# _struct.Struct.alignment

# _struct.calcsize(fmt)

# _struct.error

# _struct.pack(fmt, v1, v2, ...)
# _struct.pack_into(fmt, buffer, offset, v1, v2, ...)
# _struct.unpack(fmt, buffer)
# _struct.unpack_from(fmt, buffer, offset=0)
