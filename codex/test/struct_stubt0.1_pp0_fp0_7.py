from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack(b'\x01\x00\x00\x00')

# _struct.Struct.__new__(format)
# _struct.Struct.__init__(format)
# _struct.Struct.unpack(buffer)
# _struct.Struct.pack(v1, v2, ...)

# struct.pack(format, v1, v2, ...)
# struct.unpack(format, buffer)
# struct.calcsize(format)

# struct.Struct(format)

# struct.pack_into(format, buffer, offset, v1, v2, ...)
# struct.unpack_from(format, buffer, offset=0)

# struct.iter_unpack(format, buffer)

# struct.error

# struct.pack('>I', 10240099)
# struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')

# for c in struct.pack('>I', 10240099
