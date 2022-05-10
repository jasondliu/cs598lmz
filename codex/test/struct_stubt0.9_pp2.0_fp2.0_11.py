from _struct import Struct
s = Struct.__new__(Struct)
s.__init__(b'>HH')
s.size

s = Struct.__new__(Struct)
s.__init__(b'H')
s
s.unpack(b'!h', b'\xff\xf1')
#(bs)



import struct
struct.pack('>i',1000000000)
struct.pack('>I',1000000000)
