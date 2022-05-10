from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i?f')
s.size

s.pack(1, False, 3.14)

import struct
s = struct.Struct('i?f')
s.pack(1, False, 3.14)

data = s.pack(1, False, 3.14)
s.unpack(data)

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
	extra = data[start:start+extra_size]
	print(filename, hex(crc32), comp_size, uncomp_size)

	start += extra_size
	start += comp_size
