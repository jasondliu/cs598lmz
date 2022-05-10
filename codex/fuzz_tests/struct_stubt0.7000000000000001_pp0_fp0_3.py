from _struct import Struct
s = Struct.__new__(Struct)
s.__dict__
s.format = 'I 2s f'
s.size

import struct
struct.calcsize(s.format)

import time
time.ctime(1234567890)

from _struct import Struct
struct = Struct('>I 2s f')
struct.unpack(b'\xf0\xf0\xf0\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

struct.pack(b'\xf0\xf0\xf0\xf0', b'\x00\x00', 0.0)

struct.pack_into(b'\xf0\xf0\xf0\xf0', buff, 0, b'\x00\x00', 0.0)

import struct

with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):
    start += 14
    fields = struct.unpack('
