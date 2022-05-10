from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>H')
s.size

s.pack(0x1234)

s.unpack(_)

s.unpack_from(b'\x12\x34')

s.unpack_from(_, 0)

s.unpack_from(_, 1)

s.unpack_from(_, -1)

s.unpack_from(_, -2)

s.unpack_from(_, -3)

s.unpack_from(_, -4)

s.unpack_from(_, -5)

s.unpack_from(_, -6)

s.unpack_from(_, -7)

s.unpack_from(_, -8)

s.unpack_from(_, -9)

s.unpack_from(_, -10)

s.unpack_from(_, -11)

s.unpack_from(_, -12)

s.unpack_from(_, -13)

s.unpack_from(_, -
