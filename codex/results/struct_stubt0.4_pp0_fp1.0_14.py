from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

import sys
sys.getsizeof(s)

import array
a = array.array('i', range(5))
sys.getsizeof(a)

a.itemsize

s.pack(1, b'abc', 2.7)

s.unpack(_)

s.unpack_from(b'\x01\x00\x00\x00abc\x00\x00\x00@\x9a\x99\x99\x99\x99\x99\xf1?', 0)

s.unpack_from(b'\x01\x00\x00\x00abc\x00\x00\x00@\x9a\x99\x99\x99\x99\x99\xf1?', 4)

s.unpack_from(b'\x01\x00\x00\x00abc\x00\x00\x00@\x9a\x99\x99\x99\x99
