from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

s.pack(1, 'ab'.encode('utf-8'), 2.7)

s.unpack(_)

s.unpack_from(bytes(range(12)), 4)

import array
nums = array.array('i', range(5))
nums

nums.tobytes()

nums2 = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
nums2.frombytes(nums.tobytes())

nums2

with open('data.bin', 'wb') as f:
    f.write(nums)

with open('data.bin', 'rb') as f:
    nums3 = array.array('i')
    nums3.fromfile(f, 10)

nums3

nums == nums3

nums3 == nums2

nums3.typecode

nums3.itemsize

nums3.buffer
