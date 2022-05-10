from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack(b'\x01\x00\x00\x00')

# 使用struct模块来解决字节序问题
import struct
def to_int32(b):
    return struct.unpack('<i', b)[0]

# 将整数转换为字节
def to_bytes(n):
    return struct.pack('<i', n)

# 将整数转换为大端字节
def to_bytes_big(n):
    return struct.pack('>i', n)

# 将字节转换为大端整数
def to_int32_big(b):
    return struct.unpack('>i', b)[0]

# 将字节转换为小
