from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i?f')
s.size

s.pack(1, False, 3.14)

s.unpack(_)

s.unpack_from(bytes, 4)

import array
nums = array.array('i', [-1, -2, -3])
with open('data.num', 'wb') as f:
    f.write(nums)

a = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0])
with open('data.num', 'rb') as f:
    f.readinto(a)

a

with open('data.bin', 'wb') as f:
    f.write(b'hello world')

import os
os.stat('data.bin').st_size

with open('data.bin', 'rb') as f:
    data = f.read()

data

data[0:5]

with open('data.bin', 'rb') as f:
    f.seek(5)
    data = f.read
