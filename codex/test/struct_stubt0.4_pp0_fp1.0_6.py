from _struct import Struct
s = Struct.__new__(Struct)

s.__init__('i')

s.pack(1)

s.pack(1, 2)

s.unpack('\x01\x00\x00\x00')

s.unpack('\x01\x00\x00\x00', 1)

s.unpack_from('\x00\x00\x00\x01\x00\x00\x00\x02', 4)

s.unpack_from('\x00\x00\x00\x01\x00\x00\x00\x02', 4, 2)

s.calcsize('i')

s.pack('i', 1)

s.pack('i', 1, 2)

s.unpack('i', '\x01\x00\x00\x00')

s.unpack('i', '\x01\x00\x00\x00', 1)

