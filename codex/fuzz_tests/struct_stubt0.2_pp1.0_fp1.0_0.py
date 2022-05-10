from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I 2s f'
s.size = s.calcsize()
print(s.size)

# 创建一个结构体对象
import struct
import binascii
values = (1, 'ab'.encode('utf-8'), 2.7)
print(values)
print(binascii.hexlify(s.pack(*values)))

# 将结构体对象转换成原来的数据
print(s.unpack(b'\x01\x61\x62\x00\x00\x00\x00\x00\x00\x00\x00\xcd\xcc\x8c?\x00\x00\x00'))

# 使用大端法和小端法
s = Struct('>I 2s f')
print(binascii.hexlify(s.pack
