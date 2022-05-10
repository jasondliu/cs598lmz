from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I 2s f'
s.size = s.calcsize()
print(s.size)

# 二进制文件
import struct
import itertools

i = 0

with open('myfile.zip', 'rb') as fp:
    for chunk in iter(lambda: fp.read(10), b''):
        i += 1
        print(chunk)

print(i)

# 使用struct解析二进制数据

with open('myfile.zip', 'rb') as fp:
    data = fp.read()

start = 0
for i in range(3):
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start + filenamesize]
    start += filenamesize
    extra
