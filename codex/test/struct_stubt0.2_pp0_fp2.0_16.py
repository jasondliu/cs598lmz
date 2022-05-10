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

nums = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0])
s.pack_into(nums, 4, 1, 'ab'.encode('utf-8'), 2.7)

nums

s.unpack_from(nums, 4)

s.unpack(bytes)

s.unpack_from(bytes, 4)

s.unpack_from(bytes, 0)

s.pack(1, 'ab'.encode('utf-8'), 2.7)

