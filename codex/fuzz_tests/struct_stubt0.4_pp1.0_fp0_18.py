from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')

for i in range(10):
    print(s.pack(i))

import struct
print(struct.pack('>i', 10240099))

with open('data.bin', 'wb') as f:
    f.write(struct.pack('>i4sh', 7, b'spam', 8))

with open('data.bin', 'rb') as f:
    data = f.read()

print(data)

print(struct.unpack('>i4sh', data))

print(struct.pack('>i4sh', 7, b'spam', 8))
