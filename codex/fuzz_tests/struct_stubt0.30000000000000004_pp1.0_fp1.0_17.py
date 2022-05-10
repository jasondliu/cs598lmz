from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# struct.Struct.__new__(format)
# struct.Struct.__new__(format, *args)
# struct.Struct.__new__(format, **kwargs)
# struct.Struct.__new__(format, *args, **kwargs)

# struct.Struct.__init__(format)
# struct.Struct.__init__(format, *args)
# struct.Struct.__init__(format, **kwargs)
# struct.Struct.__init__(format, *args, **kwargs)

# struct.Struct.format
# struct.Struct.size
# struct.Struct.unpack(buffer)
# struct.Struct.unpack_from(buffer[, offset])
# struct.Struct.pack(v1[, v2[, ...]])
# struct.Struct.pack_into(buffer, offset, v1[, v2[, ...]])
# struct.Struct.iter_unpack(buffer)
# struct.Struct.iter_unpack_from(buffer
