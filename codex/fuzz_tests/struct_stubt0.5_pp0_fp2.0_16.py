from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i?f')
s.size

s = Struct('i?f')
s.size

import sys
sys.getsizeof(s)

import array
a = array.array('i', range(5))
sys.getsizeof(a)

s = Struct('i?f')
data = s.pack(1, False, 2.5)
data

data[4]

data[4] = 127

data

s.unpack(data)

s.unpack_from(data, 4)

import struct

with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
   
