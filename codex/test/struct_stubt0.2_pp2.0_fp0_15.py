from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack(b'\x01\x00\x00\x00')

# 从文件中读取格式化数据
with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):
    start += 14
    fields = unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size     # skip to the next header

# 内存映射二进制文件
import os
import mmap

