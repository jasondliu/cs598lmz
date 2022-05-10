from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack(b'\x01\x00\x00\x00')

# _struct.Struct.__new__(format)
# _struct.Struct.__init__(format)
# _struct.Struct.unpack(buffer)
# _struct.Struct.pack(v1, v2, ...)
# _struct.Struct.iter_unpack(buffer)
# _struct.Struct.size
# _struct.Struct.format
# _struct.Struct.pack_into(buffer, offset, v1, v2, ...)
# _struct.Struct.unpack_from(buffer, offset=0)
# _struct.Struct.iter_unpack_from(buffer, offset=0)

# _struct.calcsize(format)

# _struct.pack(format, v1, v2, ...)
# _struct.pack_into(format, buffer, offset, v1, v2, ...)
# _struct.unpack(format, buffer)
# _struct.unpack_from(format, buffer
