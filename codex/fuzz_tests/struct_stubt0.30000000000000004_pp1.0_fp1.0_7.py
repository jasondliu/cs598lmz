from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

s.pack(1, b'ab', 2.7)

s.unpack(_)

s.unpack_from(b'\x00\x00\x00\x01ab\x00\x00\x9a\x99\x99\x99\x99\x9a', 0)

s.unpack_from(b'\x00\x00\x00\x01ab\x00\x00\x9a\x99\x99\x99\x99\x9a', 4)

import array
nums = array.array('i', [1, 2, 3, 4])
with open('data.bin', 'wb') as f:
    f.write(nums)

a = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0])
with open('data.bin', 'rb') as f:
    f.readinto(a)

a

with open('data.bin', '
