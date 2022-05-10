from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i?f')
s.size

s.pack(1, False, 3.14)

s.unpack(_)

s.unpack_from(bytes, 4)

import array
nums = array.array('i', [1, 2, 3, 4])
s.pack_into(nums, 0, 1, False, 3.14)
nums

s.unpack_from(nums, 4)

s = Struct('i?f')
s.pack(1, False, 3.14)

import binascii
binascii.hexlify(_)

binascii.unhexlify(_)

s.unpack(_)

import io
s = Struct('i?f')
f = io.BytesIO()
s.pack_into(f, 0, 1, False, 3.14)
f.getvalue()

s.unpack_from(f.getvalue(), 0)

s.unpack(f.getvalue())

s.unpack_from(
