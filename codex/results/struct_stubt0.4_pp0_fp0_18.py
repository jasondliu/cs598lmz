from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

s.pack(1, b'ab', 2.7)

s.unpack(_)

s.unpack_from(bytes, 4)

s = Struct('I 2s f')
s.pack(1, b'ab', 2.7)

s.unpack(_)

s.unpack_from(bytes, 4)

import array
nums = array.array('i', [1, 2, 3, 4])
nums

s.pack_into(bytes, 0, *nums)

bytes

s.unpack_from(bytes, 0)

s.unpack_from(bytes, 4)

s.unpack_from(bytes, 8)

with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):
    start += 14
    fields = s.unpack_from(data, start)
    crc32, comp_size, uncomp_size =
