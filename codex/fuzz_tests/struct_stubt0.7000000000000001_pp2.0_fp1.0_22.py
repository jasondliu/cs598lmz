from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>HHIH')
s.size

s.pack(1,2,3,)

s = Struct('>HHIH')
s.unpack(b'\x00\x01\x00\x02\x00\x00\x00\x03\x00\x04')

s = Struct(b'>HHIH')
s.unpack(b'\x00\x01\x00\x02\x00\x00\x00\x03\x00\x04')

s = Struct(b'>')
s.pack(1)

s = Struct('')
s.pack()

s = Struct('l')
s.pack(1)

s = Struct(b'l')
s.pack(1)

s = Struct(b'l')
s.pack(1.0)

s = Struct('l')
s.pack(1.0)

s = Struct('l')
s.pack(1.0 + 0.0j)

s = Struct('l
