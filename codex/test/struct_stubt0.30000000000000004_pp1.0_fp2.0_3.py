from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.size

# 使用struct模块来解决字节序问题
import sys
import struct

# 如果是小端法，则输出little
# 如果是大端法，则输出big
print(sys.byteorder)

# 将数字转换为字节
x = 1234
print(x.to_bytes(2, byteorder='big'))
print(x.to_bytes(2, byteorder='little'))

# 将字节转换为数字
print(int.from_bytes(b'\x00\x0a', byteorder='big'))
print(int.from_bytes(b'\x0a\x00', byteorder='little'))

# 使用
