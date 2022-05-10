import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[3] = b'3'
    m.close()
print(mmap.allocate(10))
'''

# 读取和修改二进制数据
import struct
with open('test', 'rb') as f:
    data = f.read()
    print(data)

# 将一个字节的8位值的整数转换为一个整数
print(struct.unpack('>B', data))
# 将一个字节的8位值的整数转换为一个无符号整数
print(struct.unpack('>B', data)[0])

# 将一个字节的8位值的整数转换为一个整数
print(struct.unpack('>b
