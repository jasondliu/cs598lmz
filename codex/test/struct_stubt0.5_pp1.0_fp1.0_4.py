from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

s.pack(1, b'ab', 2.7)

s.pack(1, b'abc', 2.7)

s.unpack(_)

s.unpack(b'\x00\x00\x00\x01ab\x00\x00@B')

s.unpack(b'\x00\x00\x00\x01abcd\x00\x00@\x9a')

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
    fields = struct.unpack('>IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, fil
