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

import array
nums = array.array('i', [1, 2, 3, 4])
s.pack_into(nums, 0, 1, False, 3.14)

nums

nums = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0])
s.pack_into(nums, 2, 1, False, 3.14)

nums

s.unpack_from(nums, 2)

s.unpack_from(nums, 4)

s.unpack_from(nums, 6)

