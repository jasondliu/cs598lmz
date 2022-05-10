from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.pack(1, 'ab'.encode('utf-8'), 2.7)

from struct import Struct
s = Struct('I 2s f')
s.pack(1, 'ab'.encode('utf-8'), 2.7)

# unpack
from struct import Struct
s = Struct('I 2s f')
s.unpack(b'\x00\x00\x00\x01ab\x00\x00\x00@\x00\x00\x00')

# unpack_from
from struct import Struct
s = Struct('I 2s f')
data = b'\x00\x00\x00\x01ab\x00\x00\x00@\x00\x00\x00'
s.unpack_from(data, 8)

# calcsize
from struct import Struct
s = Struct('I 2s f')
s.calcsize()

# format
from struct import Struct
s = Struct('I 2s f')
s.format

