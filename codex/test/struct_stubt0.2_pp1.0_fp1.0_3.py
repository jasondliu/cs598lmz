from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.unpack(b'\x00\x00\x00\x00')

# 打包
s.pack(1)

# 字节流转换为整数
import struct
struct.unpack('>I', b'\x00\x00\x00\x00')

# 整数转换为字节流
struct.pack('>I', 1)

# 文件读写
with open('test.txt', 'r') as f:
    f.read()

with open('test.txt', 'rb') as f:
    f.read()

# 内存映射文件
import os
import mmap

def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
