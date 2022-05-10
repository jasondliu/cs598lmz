from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I 2s f'
s.size = s.calcsize()
print(s.size)

# 使用struct模块的pack函数来打包数据
import struct
data = struct.pack('>I 2s f', 1024, b'\x00\x01', 3.14)
print(data)

# 使用unpack函数来解包数据
print(struct.unpack('>I 2s f', data))

# 如果你想将C结构体中的数据和Python的数据互相转换，你可以使用
# 一个第三方模块，例如，CFFI和ctypes。

# 字节到大整数的打
