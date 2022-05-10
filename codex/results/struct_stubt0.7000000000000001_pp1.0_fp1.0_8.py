from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<xcb'
s.size = s.format.size
print(s.format, s.size)

print(s.pack(1, 2, 3))
print(s.unpack(b'\x00\x01\x02\x03'))

print(s.unpack_from(b'\x00\x01\x02\x03', 1))

fmt = '<3s3sHH'
with open('filter.gif', 'rb') as fp:
    img = memoryview(fp.read())

header = img[:10]
print(bytes(header))
print(Struct(fmt).unpack(header))
del header
del img

# for line in fp:
#     print(ascii(line[:10]))

import os
print(os.stat('filter.gif'))
print(os.stat('filter.gif').st_size)
print(os.stat('filter.gif').st_mode)

import time
print(time.localtime(os.
