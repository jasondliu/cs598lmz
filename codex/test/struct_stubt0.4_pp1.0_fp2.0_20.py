from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

s.pack(1, b'ab', 2.7)
s.unpack(_)

s.unpack_from(b'\x00\x00\x00\x01ab\x00\x00\x9a\x99\x99\x99\x99\x9a', 0)

s = Struct('I 2s f')
s.pack(1, b'ab', 2.7)
s.unpack(_)
s.unpack_from(b'\x00\x00\x00\x01ab\x00\x00\x9a\x99\x99\x99\x99\x9a', 0)

import array
numbers = array.array('h', [-2, -1, 0, 1, 2])
octets = bytes(numbers)
octets

import struct
struct.unpack('>5h', octets)

with open('myfile.zip', 'rb') as f:
    data = f.read
