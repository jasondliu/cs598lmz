from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

s.pack(1)

s.unpack(_)

s.unpack_from(b'\x01\x00\x00\x00', 0)

s.unpack_from(b'\x01\x00\x00\x00', 4)

s = Struct.__new__(Struct)
s.__init__('iif')
s.size

s.pack(1, 2, 3.0)

s.unpack(_)

s.unpack_from(b'\x01\x00\x00\x00\x02\x00\x00\x00'
             b'\x00\x00\x00\x00\x00\x00\xf0?', 0)

s.unpack_from(b'\x01\x00\x00\x00\x02\x00\x00\x00'
             b'\x00\x00\x00\x00\x00\x00\xf0
