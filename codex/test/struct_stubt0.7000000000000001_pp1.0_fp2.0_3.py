from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I2s f')
s.size

import os
os.stat(r'test.py').st_size

f = open('data.bin', 'wb')
import struct
data = struct.pack('>i4sh', 7, b'spam', 8)
data
f.write(data)
f.close()

f = open('data.bin', 'rb')
data = f.read()
data

struct.unpack('>i4sh', data)

s = struct.Struct('>i4sh')
s.pack(7, b'spam', 8)

f = open('data.bin', 'rb')
data = f.read()
s.unpack(data)

os.chdir('/Users/beazley/Documents/Data/data')
for filename in os.listdir('.'):
    if filename.endswith('.txt'):
        f = open(filename)
