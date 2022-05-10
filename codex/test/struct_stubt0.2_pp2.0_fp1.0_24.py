from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

# 使用struct模块来解决字节序问题
import struct
import sys

# 以小端法读取
with open('somefile.data', 'rb') as f:
    data = f.read()

start = 0
for i in range(0, len(data), 4):
    chunk = data[start:start + 4]
    start += 4
    (chunk,) = struct.unpack('<I', chunk)
    print(chunk)

# 以大端法读取
with open('somefile.data', 'rb') as f:
    data = f.read()

start = 0
for i in range(0, len(data), 4):
    chunk = data[start:start + 4]
    start += 4
    (chunk,) = struct.unpack('>I', chunk)
    print(chunk)

# 使
