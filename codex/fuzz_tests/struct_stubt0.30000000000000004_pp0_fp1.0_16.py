from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# 使用struct模块来解决字节序问题
import sys
import struct

# 将一个32位无符号整数转换为字节
def int32_to_bytes(n):
    return struct.pack('I', n)

# 将一个字节转换为32位无符号整数
def bytes_to_int32(b):
    return struct.unpack('I', b)[0]

# 将一个16位无符号整数转换为字节
def int16_to_bytes(n):
    return struct.pack('H', n)

# 将一个字节转换为16位
