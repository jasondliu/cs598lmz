from _struct import Struct
s = Struct.__new__(Struct)
s.size = 0
print(s.size)

# 3.2.6
s = Struct('i?f')
print(s.size)

# 3.2.7
import struct
values = (1, 'ab', 2.7)
print(struct.pack('>I2sf', *values))

# 3.2.8
print(struct.unpack('>I2sf', b'\x00\x00\x00\x01ab\x00\x00\x00\x00\x00\x00@\x00\x00'))

# 3.2.9
with open('myfile.zip', 'rb') as f:
    data = f.read()
start = 0
for i in range(3):
    start += 14
    fields = struct.unpack('>IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
