from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

s = Struct('i')
s.size

s = Struct('i')
s.pack(1)

s = Struct('i')
s.unpack(b'\x01\x00\x00\x00')

s = Struct('i')
s.unpack_from(b'\x01\x00\x00\x00', 0)

s = Struct('i')
s.unpack_from(b'\x01\x00\x00\x00', 0)

s = Struct('i')
s.unpack_from(b'\x01\x00\x00\x00', 0)

s = Struct('i')
s.unpack_from(b'\x01\x00\x00\x00', 0)

s = Struct('i')
s.unpack_from(b'\x01\x00\x00\x00', 0)

s = Struct('i')
s.unpack_from(b'\x01
