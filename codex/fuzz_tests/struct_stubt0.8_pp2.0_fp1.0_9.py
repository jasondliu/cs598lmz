from _struct import Struct
s = Struct.__new__(Struct)
s
list(s)
s.format = '2h l 5sh f'
s.size
s.pack(1,2,3,4,5,6,7,8,9)
s.unpack(_)
s.unpack(_)
s.unpack(b'\x00\x01\x00\x02\x00\x00\x00\x03\x00\x04\x00\x05\x00\x06\x00\x07\x00\x08\t')
s.unpack(b'\x00\x01\x00\x02\x00\x00\x00\x03\x00\x04\x00\x05\x00\x06\x00\x07\x00\x08\t')
 
from _struct import calcsize
calcsize(s.format)
s = Struct('i?f')
s.size
s.pack(1, 0, 3.14159)
s.unpack(_)
s.unpack(b'\x01
