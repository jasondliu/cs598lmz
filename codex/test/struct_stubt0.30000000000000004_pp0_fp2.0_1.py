from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

s.pack(1, 'ab'.encode('utf-8'), 2.7)

# struct.Struct.unpack(buffer)
s.unpack(_)

s.unpack_from(buffer, 4)

# struct.Struct.iter_unpack(buffer)
list(s.iter_unpack(buffer))

# struct.Struct.unpack_from(buffer, offset=0)
s.unpack_from(buffer, 4)

# struct.Struct.iter_unpack(buffer)
list(s.iter_unpack(buffer))

# struct.Struct.pack_into(buffer, offset, v1, v2, ...)
s.pack_into(buffer, 0, 1, 'ab'.encode('utf-8'), 2.7)

# struct.Struct.unpack_from(buffer, offset=0)
s.unpack_from(buffer, 0)

# struct.Struct.unpack(buffer)
s.unpack(_)

# struct
