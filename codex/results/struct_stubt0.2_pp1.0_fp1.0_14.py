from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack(b'\x01\x00\x00\x00')

# _struct.Struct.__new__(format)
# _struct.Struct.__init__(format)
# _struct.Struct.pack(v1, v2, ...)
# _struct.Struct.unpack(buffer)
# _struct.Struct.iter_unpack(buffer)
# _struct.Struct.size
# _struct.Struct.format
# _struct.Struct.pack_into(buffer, offset, v1, v2, ...)
# _struct.Struct.unpack_from(buffer, offset=0)
# _struct.Struct.iter_unpack_from(buffer, offset=0)
# _struct.Struct.unpack_from_iter(buffer_iterator, offset=0)
# _struct.Struct.unpack_from_buffer(buffer, offset=0)
# _struct.Struct.unpack_from_buffer_copy(buffer, offset=0)
# _struct.Struct.get_format_iter(format
