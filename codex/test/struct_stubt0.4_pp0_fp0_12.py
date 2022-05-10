from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
print(s.size)
print(s.pack(1, b'ab', 2.7))
print(s.unpack(b'\x01ab\x00\x00\x00\x00\x00\x00\xcd\xcc\x8c?\x00'))

# 将结构体编码为二进制字符串
import struct

with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):  # 打印前3个文件头
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
