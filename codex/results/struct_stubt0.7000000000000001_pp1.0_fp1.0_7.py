from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

import struct
struct.calcsize('I 2s f')

octets = s.pack(303, b'\0xab', 3.14)
octets

s.unpack(octets)

import struct
with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size

# 格式化字节字符串

#
