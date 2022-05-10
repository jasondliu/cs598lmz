from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

s.pack(1, 'ab'.encode('utf-8'), 2.7)

s.unpack(_)

s.unpack_from(b'\x01\x00\x00\x00ab\x00\x00\x00@\x9a\x99\x99\x99\x99\x9a', 0)

s.unpack_from(b'\x01\x00\x00\x00ab\x00\x00\x00@\x9a\x99\x99\x99\x99\x9a', 4)

# ### Named Structures

import struct

struct.Struct('i?f')

struct.Struct('i?f')

struct.Struct('i?f')

struct.Struct('i?f')

struct.Struct('i?f')

struct.Struct('i?f')

struct.Struct('i?f')

struct.Struct('i?f')

struct.
