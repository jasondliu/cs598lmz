from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

s.pack(1, 'ab'.encode('utf-8'), 2.7)

s.unpack(_)

s.unpack_from(bytes(range(12)), 4)

s = Struct('I 2s f')
s.pack(1, 'ab'.encode('utf-8'), 2.7)

s.unpack(_)

s.unpack_from(bytes(range(12)), 4)

import array

numbers = array.array('h', [-2, -1, 0, 1, 2])
octets = bytes(numbers)
octets

import struct

struct.unpack('>5h', octets)

with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, fil
