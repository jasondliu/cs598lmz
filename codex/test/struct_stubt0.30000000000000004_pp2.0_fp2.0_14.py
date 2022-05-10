from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.pack(1, 'ab'.encode('utf-8'), 2.7)

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
# struct.Struct.unpack(buffer, _error=None)
# struct.Struct.iter_unpack(buffer, _error=None)

# struct.pack(fmt, v1, v2, ...)
# struct.unpack(fmt, buffer)
# struct.iter_unpack(fmt, buffer)
# struct.calcsize
