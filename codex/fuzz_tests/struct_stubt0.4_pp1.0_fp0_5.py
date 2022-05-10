from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>H')
s.size

s.pack(1)

s.unpack(b'\x00\x01')

s.unpack_from(b'\x00\x01\x02\x03', 2)

s = Struct('>H')
s.size

s.pack(1)

s.unpack(b'\x00\x01')

s.unpack_from(b'\x00\x01\x02\x03', 2)

s = Struct('>H')
s.size

s.pack(1)

s.unpack(b'\x00\x01')

s.unpack_from(b'\x00\x01\x02\x03', 2)

s = Struct('>H')
s.size

s.pack(1)

s.unpack(b'\x00\x01')

s.unpack_from(b'\x00\x01\x02\x03', 2)


