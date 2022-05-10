from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

s.pack(1, 'ab'.encode('utf-8'), 2.7)

s.unpack(_)

s.unpack_from(bytes, 4)

import array
nums = array.array('i', [1, 2, 3, 4])
s.pack_into(nums, 0, 1, 'ab'.encode('utf-8'), 2.7)

nums

with open('data.bin', 'wb') as f:
    f.write(s.pack(1, 'ab'.encode('utf-8'), 2.7))

with open('data.bin', 'rb') as f:
    d = f.read()

s.unpack(d)

import struct
struct.pack('>I', 10240099)

struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')

struct.pack('>IH', 10240099, 10240099)

