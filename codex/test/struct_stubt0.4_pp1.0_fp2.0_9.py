from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

s.pack(1, 'ab', 2.7)

s.unpack(_)

s.unpack_from(bytes, 4)

s = Struct('I 2s f')
s.unpack_from(bytes, 4)

import array
nums = array.array('i', [1, 2, 3, 4])
s.pack_into(bytes, 0, *nums)

bytes

s.unpack_from(bytes, 0)

s.unpack(bytes)

s = Struct('iif')
s.size

s.pack(1, 2, 3.0)

s.pack_into(bytes, 0, 1, 2, 3.0)

bytes

s.unpack(bytes)

s.unpack_from(bytes, 0)

s.unpack_from(bytes, 4)

s.unpack_from(bytes, 8)

# %load './code/struct_calcsize.py'
