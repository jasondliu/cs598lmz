from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

import struct
struct.calcsize('I 2s f')

data = struct.pack('I 2s f', 1, b'ab', 2.7)
data

struct.unpack('I 2s f', data)

# 二进制文件
# 写入
with open('data.bin', 'wb') as f:
    f.write(b'\x00\x00\x00\x07spam\x00\x08')

# 读取
with open('data.bin', 'rb') as f:
    data = f.read()
data

# 文本文件
# 写入
with open('data.txt', 'w') as f:
    f.write('Hello World\n')

# 读取
with open('data.txt', 'r') as f:
    data = f.read()
data

# 写入
with open('
