from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

s.pack(1)

s.unpack(_)

s.unpack_from(b'\x00\x00\x00\x01', 0)

s.unpack_from(b'\x00\x00\x00\x01\x00\x00\x00\x02', 0)

s.unpack_from(b'\x00\x00\x00\x01\x00\x00\x00\x02', 4)

import array
a = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0])

memoryview(a).cast('B')

m = _
m[4] = 1
m[5] = 2
a

import binascii
binascii.hexlify(a)

a = array.array('i', [0, 0, 0, 0])
m = memoryview(a).cast('B')
m[0] = 1
m[1]
