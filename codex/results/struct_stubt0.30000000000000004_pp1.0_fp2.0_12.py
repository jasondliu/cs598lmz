from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.unpack(b'\x00\x00\x00\x00')

# This is the same as the above.
Struct('>I').unpack(b'\x00\x00\x00\x00')

# This is the same as the above.
Struct('>I').unpack_from(b'\x00\x00\x00\x00')

# This is the same as the above.
Struct('>I').unpack_from(b'\x00\x00\x00\x00', 0)

# This is the same as the above.
Struct('>I').unpack_from(b'\x00\x00\x00\x00', 0)

# This is the same as the above.
Struct('>I').unpack_from(b'\x00\x00\x00\x00', 0)

# This is the same as the above.
Struct('>I').unpack_from(b'\x00\x00\x00\x
