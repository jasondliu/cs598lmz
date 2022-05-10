from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

s.pack(1, 'ab'.encode('utf-8'), 2.7)

s.unpack(_)

s.unpack_from(bytes(range(12)), 4)

import array
nums = array.array('i', [1, 2, 3, 4])
s.pack_into(nums, 0, 1, 'ab'.encode('utf-8'), 2.7)

nums

s.unpack_from(_, 0)

s.unpack_from(_, 4)

s = Struct.__new__(Struct)
s.__init__('>I 2s f')
s.size

s.pack(1, 'ab'.encode('utf-8'), 2.7)

s.unpack(_)

s.unpack_from(bytes(range(12)), 4)

import array
nums = array.array('i', [1, 2, 3, 4])
s.pack_into(nums, 0, 1,
