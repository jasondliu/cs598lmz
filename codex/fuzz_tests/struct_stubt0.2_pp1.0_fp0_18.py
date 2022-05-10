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

nums.tobytes()

s.unpack_from(nums.tobytes(), 4)

s.unpack_from(nums.tobytes(), 8)

import struct
struct.pack('>I 2s f', 1, 'ab'.encode('utf-8'), 2.7)

struct.unpack('>I 2s f', _)

struct.pack('>I 2s f', *(1, 'ab'.encode('utf-8'), 2.7))

struct.unpack('>I 2s f', _)

struct.un
