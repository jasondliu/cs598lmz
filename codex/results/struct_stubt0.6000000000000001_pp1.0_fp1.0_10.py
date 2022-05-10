from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'HhL'
s.size = 8

print s.unpack('\x00\x01\x00\x02\x00\x00\x00\x03')
print s.unpack_from('\x00\x01\x00\x02\x00\x00\x00\x03', offset=2)

print s.pack(1, 2, 3)
print s.pack_into('\x00\x00\x00\x00\x00\x00\x00\x00', offset=2, v1=1, v2=2, v3=3)

print s.unpack_from(buffer('\x00\x01\x00\x02\x00\x00\x00\x03'), offset=2)

s = Struct.__new__(Struct)
s.format = 'hhl'
s.size = 8
print s.unpack_from(buffer('\x00\x01\x00\x02\x00\x00\x00\x03
