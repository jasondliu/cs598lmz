from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i?f')
s.size

s.pack(1, False, 3.14)

s.unpack(_)

s.unpack_from(bytes, 4)

s = Struct('i?f')
s.pack(1, False, 3.14)

s.unpack(_)

s.unpack_from(bytes, 4)

import struct
struct.pack('>i?f', 1, False, 3.14)

struct.unpack('>i?f', _)

struct.unpack('>i?f', bytes)

struct.unpack_from('>i?f', bytes, 4)

import array
nums = array.array('i', [1, 2, 3, 4])

with open('data.bin', 'wb') as f:
    f.write(nums)

nums

import array
a = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0])

