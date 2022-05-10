from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

s = Struct('i')
s.size

s = Struct('i')
s.pack(1)

s.unpack(b'\x01\x00\x00\x00')

s.unpack_from(b'\x01\x00\x00\x00abc', 0)

s.unpack_from(b'\x01\x00\x00\x00abc', 4)

s.pack_into(b'\x00'*8, 4, 1)

s.pack_into(b'\x00'*8, 0, 1)

s.calcsize()

s.pack(1)

s.pack(1, 2, 3)

s.unpack(s.pack(1, 2, 3))

s.unpack(b'\x01\x00\x00\x00')

s.unpack_from(b'\x01\x00\x00\x00abc', 0)

