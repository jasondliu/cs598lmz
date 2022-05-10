from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

s.pack(1, b'ab', 2.7)

s.unpack(_)

s.unpack_from(b'\x01\x00\x00\x00ab\x00\x00\x00@\x9a\x99\x99\x99\x99\x9a')

s.unpack_from(_, 4)

s.unpack_from(_, 8)

import array
numbers = array.array('h', [-2, -1, 0, 1, 2])
octets = bytes(numbers)
octets

import struct
struct.unpack('>5h', octets)

for n in numbers:
    print(n)

with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):
    start += 14
