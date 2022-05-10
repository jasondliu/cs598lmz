from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

s.pack(1, 'ab', 2.7)

s.unpack(_)

s.unpack_from(b'\x00\x00\x00\x01ab\x00\x00\x00@', 0)

s.unpack_from(b'\x00\x00\x00\x01ab\x00\x00\x00@', 4)

s.unpack_from(b'\x00\x00\x00\x01ab\x00\x00\x00@', 5)

import array

numbers = array.array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
len(memv)

memv[0]

memv_oct = memv.cast('B')
memv_oct.tolist()

memv_oct[5] = 4
numbers

import sys
sys.getsizeof(5)
