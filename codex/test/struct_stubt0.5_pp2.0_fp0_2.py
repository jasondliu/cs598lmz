from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

s.pack(1, 'ab'.encode('utf-8'), 3.0)

s.unpack(_)

s.unpack_from(bytes(range(12)), 4)

s = Struct('I 2s f')
s.unpack(b'\x00\x00\x00\x01ab\x00\x00\x00')

import struct
struct.pack('>I', 10240099)

struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')

struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')

for code in [b'<HH', b'!HH']:
    print(struct.unpack(code, b'\x00\x01\x00\x02'))

import binascii
binascii.crc32(b'hello world')

binas
