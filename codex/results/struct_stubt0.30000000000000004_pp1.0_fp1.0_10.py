from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.unpack(b'\x00\x00\x00\x01')

# 使用struct模块来解决字节序问题
import struct
struct.pack('>I', 10240099)

# 字节序转换
x = 0x01020304
x.to_bytes(4, byteorder='big')
x.to_bytes(4, byteorder='little')

# 使用int.from_bytes()来解决字节序问题
data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
int.from_bytes(data, 'little')
int.from_bytes(data, 'big')

# 字节序转换
x = 0x01020304
