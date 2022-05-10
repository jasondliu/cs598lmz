from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>H')
s.size

s.pack(1)

s.pack(1)

s.unpack(b'\x00\x01')

s.unpack(b'\x01\x00')

s.unpack(b'\x00\x01')

s.unpack(b'\x01\x00')

s.pack(1)

s.pack(1)

s.unpack(b'\x00\x01')

s.unpack(b'\x01\x00')

s.unpack(b'\x00\x01')

s.unpack(b'\x01\x00')

s.pack(1)

s.pack(1)

s.unpack(b'\x00\x01')

s.unpack(b'\x01\x00')

s.unpack(b'\x00\x01')

s.unpack(b'\x01\x00')

