from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i?f')
s.size

s.pack(1, False, 3.14)

s.unpack(_)

s.unpack_from(bytes, 4)

import array
nums = array.array('i', [1, 2, 3, 4])
s.pack_into(nums, 0, 1, False, 3.14)
nums

s.unpack_from(nums, 4)

with open('data.bin', 'wb') as f:
    s.pack_into(f, 0, 1, False, 3.14)

with open('data.bin', 'rb') as f:
    s.unpack(f.read())

with open('data.bin', 'rb') as f:
    s.unpack_from(f.read(), 0)

with open('data.bin', 'rb') as f:
    s.unpack_from(f.read(), 4)

with open('data.bin', 'rb') as f:
    s.unpack_from(
