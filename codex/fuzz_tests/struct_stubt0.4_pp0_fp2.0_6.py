from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

s.pack(1, 'ab'.encode('utf-8'), 2.7)

s.unpack(_)

s.unpack_from(bytes(range(12)), 4)

s = Struct('I 2s f')
s.pack(1, 'ab'.encode('utf-8'), 2.7)

with open('data.bin', 'wb') as f:
    f.write(s.pack(1, 'ab'.encode('utf-8'), 2.7))

with open('data.bin', 'rb') as f:
    data = f.read()

s.unpack(data)

s.unpack_from(data, 4)

s.iter_unpack(data)

for rec in s.iter_unpack(data):
    print(rec)

import array

nums = array.array('i', [1, 2, 3, 4])

with open('data.bin', 'wb') as f:
    f.
