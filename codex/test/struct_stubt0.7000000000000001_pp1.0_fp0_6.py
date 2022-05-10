from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
print(s.size)
print(s.pack(1))
print(s.unpack(b'\x01\x00\x00\x00'))
print(s.unpack_from(bytes(4), 0))

## 
print('{:<30}'.format('struct.pack()'))
print(struct.pack('i', 1))
print('{:<30}'.format('struct.pack_into()'))
print(struct.pack_into('i', bytearray(1), 0, 1))
print('{:<30}'.format('struct.unpack()'))
print(struct.unpack('i', b'\x01\x00\x00\x00'))
print('{:<30}'.format('struct.unpack_from()'))
print(struct.unpack_from('i', b'\x01\x00\x00\x00', 0))

## 
print('{:<30}'.format('struct.calcsize()'))

