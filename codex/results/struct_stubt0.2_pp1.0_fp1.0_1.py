from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I 2s f'
s.size = s.calcsize(s.format)
print(s.size)

# 创建一个结构体对象
import struct
import binascii
values = (1, 'ab'.encode('utf-8'), 2.7)
print(values)
print(binascii.hexlify(struct.pack('I 2s f', *values)))

# 将结构体对象解析为原来的数据
print(struct.unpack('I 2s f', b'\x01\x00\x00\x00ab\x00\x00\x00\x00\x00\x00(B'))

# 将结构体对象解析为原来的数据
with open('data.b', 'rb') as f:

