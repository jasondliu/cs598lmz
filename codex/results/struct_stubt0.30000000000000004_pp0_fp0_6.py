from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

s.pack(1, b'ab', 2.7)

s.unpack(_)

s.unpack_from(b'\x01\x00\x00\x00ab\x00\x00\x00@\x9a\x99\x99\x99\x99\x9a')

import array
nums = array.array('i', [1, 2, 3, 4])
with open('data.bin', 'wb') as f:
    f.write(nums)

a = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0])
with open('data.bin', 'rb') as f:
    f.readinto(a)

a

with open('sample.bin', 'wb') as f:
    f.write(b'Hello World')

import os
st = os.stat('sample.bin')
st.st_size

with open('sample.bin', 'rb') as f
