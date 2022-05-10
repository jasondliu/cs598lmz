from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I 2s f'
s.size = s.calcsize()

print(s.size)
print(s.pack(1, b'ab', 2.7))

# 使用struct模块来解决字节序问题
import sys
import struct

# 小端法
print(sys.byteorder)

# 大端法
print(sys.byteorder == 'big')

# 小端法
print(sys.byteorder == 'little')

# 小端法
print(struct.pack('=H', 1))

# 大端法
print(struct.pack('>H', 1))

# 小端法
print(struct.unpack('=H', b'\x00\x01'))

# 大端法
print(struct.unpack('>H', b'\x00\x01'))

# 小
