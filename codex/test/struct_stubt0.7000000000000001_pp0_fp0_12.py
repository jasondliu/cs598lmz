from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<H')
s.size

s = Struct('<H')
s
s.size
s.format
s = Struct('<2H')
s.size

import struct
struct_c = struct.Struct('<H')
with open('binary_file.bin', 'rb') as f:
    data = f.read(struct_c.size)
values = struct_c.unpack(data)
values

struct_c = struct.Struct('<2H')
with open('binary_file.bin', 'rb') as f:
    data = f.read(struct_c.size)
values = struct_c.unpack(data)
values

struct_c = struct.Struct('<I')
with open('binary_file.bin', 'rb') as f:
    data = f.read(struct_c.size)
values = struct_c.unpack(data)
values

import os
os.path.getsize('binary_file.bin')

