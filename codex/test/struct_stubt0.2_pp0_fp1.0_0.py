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
s.pack_into(bytes, 0, *nums)

bytes

s.unpack_from(bytes, 0)

s.unpack_from(bytes, 4)

s.unpack_from(bytes, 8)

s.unpack_from(bytes, 12)

s = Struct('i?f')
s.pack_into(bytes, 0, 1, False, 3.14)

bytes

s.unpack_from(bytes, 0)

s.unpack_from(bytes, 4)

