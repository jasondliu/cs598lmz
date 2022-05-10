from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.size
s.pack(1)
s.unpack(b'\x00\x00\x00\x01')
s.unpack(b'\x00\x00\x00\x01')[0]
s.unpack(b'\x00\x00\x00\x01')[0] == 1
s.unpack(b'\x00\x00\x00\x01')[0] == 2
s.unpack(b'\x00\x00\x00\x01')[0] == 3
s.unpack(b'\x00\x00\x00\x01')[0] == 4
s.unpack(b'\x00\x00\x00\x01')[0] == 5
s.unpack(b'\x00\x00\x00\x01')[0] == 6
s.unpack(b'\x00\x00\x00\x01')[0] == 7
