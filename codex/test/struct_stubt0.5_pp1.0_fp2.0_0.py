from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<i'
s.size = 4
s.unpack_from(b'\x00\x00\x00\x0a', 0)

# 使用struct模块
# 将一个字节流解析成Python类型
import struct
struct.unpack('<i', b'\x00\x00\x00\x0a')

# 将Python类型打包成一个字节流
struct.pack('<i', 10)

# 将Python类型打包成一个字节流并写入文件
import struct
with open('data.bin', 'wb') as f:
    f.write(struct.pack('<i', 10))

# 读取文件中的字节流并解析成Python
