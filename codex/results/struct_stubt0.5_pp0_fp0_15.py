from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i?f')
s.size

s.pack(1, False, 3.14)

s.unpack(_)

s.unpack_from(bytes, 4)

s.unpack_from(bytes)

import array
nums = array.array('i', [1, 2, 3, 4])
s.pack_into(bytes, 0, *nums)

bytes

bytes[4:]

s.unpack_from(_, 0)

with open('data.bin', 'wb') as f:
    f.write(bytes)

with open('data.bin', 'rb') as f:
    data = f.read()

data

s.unpack_from(data, 0)

with open('data.bin', 'rb') as f:
    for chunk in iter(lambda: f.read(8), b''):
        print(s.unpack(chunk))

with open('data.bin', 'rb') as f:
    for chunk in iter(lambda: f.read(
