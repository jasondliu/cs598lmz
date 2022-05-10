from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

s.pack(1, 'ab'.encode('utf-8'), 3.0)

s.unpack(_)

s.unpack_from(bytes(range(12)), 4)

import array
nums = array.array('i', range(5))
s.pack_into(bytes(10), 0, 1, b'ab', 3.0)

nums

s.unpack_from(bytes(10), 0)

s.unpack_from(bytes(10), 4)

s.unpack_from(bytes(10), 8)

import sys
sys.byteorder

s = Struct('>I 2s f')
s.pack(1, b'ab', 3.0)

s.unpack(_)

s.unpack(b'\x00\x00\x00\x01ab\x00\x00\x80?\x00\x00\x00\x00\x00\x00')

s.unpack(
