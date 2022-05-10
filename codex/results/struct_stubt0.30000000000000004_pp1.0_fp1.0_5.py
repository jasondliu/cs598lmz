from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I 2s f'
s.size = s.calcsize(s.format)
print(s.size)

# 创建结构体对象
import struct
import binascii
values = (1, 'ab'.encode('utf-8'), 2.7)
print(values)
print(struct.pack(s.format, *values))
print(binascii.hexlify(struct.pack(s.format, *values)))

# 解析结构体
print(struct.unpack(s.format, b'\x01\x00\x00\x00ab\x00\x00\x00\x00\x00\x00(B'))

# 将结构体对象写入文件
with open('data.b', 'wb') as f:
    f.write(struct.pack(s.format, *values))

# 
