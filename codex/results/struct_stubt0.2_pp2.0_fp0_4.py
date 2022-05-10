from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

s.pack(1, 'ab'.encode('utf-8'), 2.7)

s.unpack(_)

s.unpack_from(b'\x00\x00\x00\x01ab\x00\x00\x00@\x00\x00\x00', 0)

s.unpack_from(b'\x00\x00\x00\x01ab\x00\x00\x00@\x00\x00\x00', 4)

import array
nums = array.array('i', [1, 2, 3, 4])
nums

a = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0])
a

a[2:5] = nums
a

a[2:5] = array.array('i', [7, 8, 9])
a

a[2:5] = [7, 8, 9]
a

a[2:5
