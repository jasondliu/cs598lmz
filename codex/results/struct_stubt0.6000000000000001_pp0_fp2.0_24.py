from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.unpack_from(b'\x00\x00\x00\x00', 0)

# EOF
