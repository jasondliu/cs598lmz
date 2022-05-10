from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

s.pack(1, b'ab', 2.7)

s.unpack(b'\x01\x00\x00\x00ab\x00\x00\x00@')

s.unpack_from(b'\x01\x00\x00\x00ab\x00\x00\x00@\x02\x00\x00\x00cd\x00\x00\x08@', 4)

s = Struct('I 2s f')
s.pack(1, b'ab', 2.7)

s.unpack(b'\x01\x00\x00\x00ab\x00\x00\x00@')

s.unpack_from(b'\x01\x00\x00\x00ab\x00\x00\x00@\x02\x00\x00\x00cd\x00\x00\x08@', 4)

import array
nums = array.array
