from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'BBBBB'
s.unpack('\x01\x02\x03\x04\x05')

s = Struct.__new__(Struct)
s.format = 'HiHi'
s.unpack(b'ABCDABCD')
