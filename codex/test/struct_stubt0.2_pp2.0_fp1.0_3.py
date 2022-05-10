from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I 2s f'
s.size = s.calcsize()
print(s.size)

# 创建一个结构体对象，并将其写入文件
import struct
f = open('data.bin', 'wb')
data = struct.pack('>iif', 1, b'br', 2.7)
f.write(data)
f.close()

# 读取文件中的结构体数据
f = open('data.bin', 'rb')
data = f.read()
values = struct.unpack('>iif', data)
print(values)

# 使用结构体格式化数据
s = Struct('>iif')
with open('data.bin', 'rb') as f:
    data = f.read(s.size)
    print(s.unpack(data))
