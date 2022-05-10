from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

s.pack(1, 'ab'.encode('ascii'), 2.7)

s.unpack(_)

s.unpack_from(b'\x00\x00\x00\x01ab\x00\x00\x00@\x00\x00\x00', 0)

s.unpack_from(b'\x00\x00\x00\x01ab\x00\x00\x00@\x00\x00\x00', 4)

import array
nums = array.array('i', [1, 2, 3, 4])
nums

with open('data.bin', 'wb') as f:
    f.write(nums)

a = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0])
with open('data.bin', 'rb') as f:
    f.readinto(a)

a

with open('data.bin', 'rb') as f
