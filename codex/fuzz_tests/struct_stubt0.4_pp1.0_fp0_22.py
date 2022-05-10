from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I 2s f'
s.size = s.calcsize(s.format)
print(s.size)

# 创建了一个空的结构体，然后设置格式，最后计算结构体的大小

# 将数据打包成结构体
import struct
packed_data = struct.pack('>i4sh', 7, b'spam', 8)
print(packed_data)

# 拆包
import struct
original_data = struct.unpack('>i4sh', packed_data)
print(original_data)

# 将结构体写入文件
import struct
with open('data.bin', 'wb') as f:
    f.write(struct.pack('>i4sh', 7, b'sp
