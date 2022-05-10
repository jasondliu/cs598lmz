from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack(b'\x00\x00\x00\x00')

# struct.unpack_from(fmt, buffer[, offset=0])
# struct.pack_into(fmt, buffer, offset, v1, v2, ...)
# struct.calcsize(fmt)

# struct.error

# struct.pack(fmt, v1, v2, ...)
# struct.unpack(fmt, buffer)

# struct.Struct(fmt)

# struct.__doc__

# struct.__name__

# struct.__package__
