from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

s.pack(1, 'ab', 2.7)

s.unpack(_)

s.unpack_from(buffer('\x01\x00\x00\x00ab\x00\x00\x00@'), 0)

s.unpack_from(buffer('\x01\x00\x00\x00ab\x00\x00\x00@'), 4)

s.unpack_from(buffer('\x01\x00\x00\x00ab\x00\x00\x00@'), 5)

s.unpack_from(buffer('\x01\x00\x00\x00ab\x00\x00\x00@'), 6)

s.unpack_from(buffer('\x01\x00\x00\x00ab\x00\x00\x00@'), 7)

