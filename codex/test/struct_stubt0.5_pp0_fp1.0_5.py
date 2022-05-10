from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

calcsize('I 2s f')

s.pack(1, 'spam', 3.0)

s.unpack(_)

s.pack('spam', 3.0, 1)

s.unpack(_)

s.pack(b'\x01\x02\x03\x04\x05', b'\x06\x07\x08\x09', b'\x0a\x0b\x0c\x0d')

s.unpack(_)

s.pack(1, 'spam', 3.0)

s.pack_into(_, 0, 1, 'spam', 3.0)

s.unpack_from(_, 0)

s.unpack_from(_, 4)

s.unpack_from(_, 8)

s.unpack_from(_, 1)

import array

a = array.array('i', range(5))
a

