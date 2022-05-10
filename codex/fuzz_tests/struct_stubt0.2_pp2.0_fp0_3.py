from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I 2s f'
s.size = s.calcsize()
print(s.size)

import struct
print(struct.calcsize('I 2s f'))

with open('data.bin', 'wb') as f:
    f.write(b'\x00\x00\x00\x07spam\x00\x08\x00\x00')

with open('data.bin', 'rb') as f:
    data = f.read()

print(data)

print(struct.unpack('>I 2s f', data))

print(struct.pack('>I', 10240099))

print(struct.unpack('>I', b'\x00\x9c@c'))

print(struct.pack('>I', 10240099))

print(struct.unpack('>I', b'\x00\x9c@c'))

print(struct.unpack('>IH', b'\x00\x9c@c'))

print(struct
