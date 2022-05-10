from _struct import Struct
s = Struct.__new__(Struct)
s.__setattr__('format','I 2s f')
s.__setattr__('size', calcsize('I 2s f'))
print(s.size)
print(s.format)
print(s.unpack(b'\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'))

f = open('./test.bin','rb')
print(s.unpack(f.read(s.size)))
