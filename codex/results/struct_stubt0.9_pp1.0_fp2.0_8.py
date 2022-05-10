from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i?f')
s.size

s = Struct('i?f')
s.size

import struct
fmt = '<3s3sHH'
with open('filter.gif', 'rb') as fp:
  img = memoryview(fp.read(10))
struct.pack(fmt, img)

struct.unpack(fmt, b'GIF89a\x01\x00\x01\x00')

del img

struct.unpack(fmt, b'GIF89a\x01\x00\x01\x00')

import struct

def write_records(records, format, f):
    for fields in records:
        block = struct.pack(format, *fields)
        f.write(block)

with open('data2.b', 'wb') as f:
    records =[(1, 2.3, 4.5),
              (6, 7.8, 9.0),
              (12, 13.4, 56.7)]
    write_rec
