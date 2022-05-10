from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>H')
s.size

s.pack(255)

s.pack(256)

s.unpack(_)

s.unpack(b'\x00\xff')

s.unpack(b'\xff\x00')

s.unpack(b'\x00\x00')

s.unpack(b'\xff\xff')

s.unpack(b'\x01\x00')

s.unpack(b'\x00\x01')

s = Struct.__new__(Struct)
s.__init__('>I')
s.size

s.pack(2**32-1)

s.pack(2**32)

s.unpack(_)

s.unpack(b'\xff\xff\xff\xff')

s.unpack(b'\x00\x00\x00\x00')

s.unpack(b'\x01\x00\x00\x00')

s.unpack(
