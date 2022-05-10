from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

s.pack(1, b'ab', 2.7)

s.unpack(_)

s.unpack_from(bytes, 4)

s.unpack_from(bytes)

import array
nums = array.array('i', [1, 2, 3, 4])
s.pack_into(bytes, 0, *nums)

bytes

s.unpack_from(_, 4)

s.unpack_from(_)

nums

nums.tobytes()

s.unpack(nums.tobytes())

s = Struct('i?f')
s.unpack(b'\x12\x01\x00\x00\x00\x00\x00\x00')

s.unpack(b'\x12\x00\x00\x00\x00\x00\x00\x00')

s = Struct('P')
s.pack(b'abc')

