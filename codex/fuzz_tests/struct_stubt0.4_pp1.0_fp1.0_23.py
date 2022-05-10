from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>H')
s.size

# 使用struct模块来解决字节序问题
import sys
import struct

# Little-endian
print(sys.byteorder)

# Big-endian
print(sys.byteorder == 'big')

# Little-endian
print(struct.pack('>H', 1))

# Big-endian
print(struct.pack('<H', 1))

# Little-endian
print(struct.pack('>H', 1))

# Big-endian
print(struct.pack('<H', 1))

# Little-endian
print(struct.unpack('>H', b'\x00\x01'))

# Big-endian
print(struct.unpack('<H', b'\x00\x01'))

# Little-endian
print(struct.unpack('>H', b'\x00\x01'))

# Big-endian
print
