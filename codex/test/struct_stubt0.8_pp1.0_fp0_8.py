from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i?f')
s.size

s = Struct('i?f')
s.size

s.pack(1, False, 2.71828)
s.unpack(_)

s.unpack(s.pack(1, False, 2.71828))

s.pack(1, 2, 3)

s = Struct('i?f')
octets = s.pack(1, False, 2.71828)
octets

octets = b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\t!\x18@'
octets

octets = b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\t!\x18@'
octets = b'\x01\x00\x00\x00\x00\x00\x00\x00'
octets

