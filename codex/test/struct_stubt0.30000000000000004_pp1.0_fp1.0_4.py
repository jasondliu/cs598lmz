from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

s.pack(1, 'ab'.encode('utf-8'), 2.7)

s.unpack(_)

s.unpack_from(bytes, 4)

s = Struct('I 2s f')
s.pack(1, 'ab'.encode('utf-8'), 2.7)

s.unpack(_)

s.unpack_from(bytes, 4)

import struct
struct.pack('>I', 10240099)

struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')

struct.pack('>IH', 10240099, 1024)

struct.unpack('>IH', _)

for char in b'\xf0\xf0\xf0\xf0\x80\x80':
    print(char)

