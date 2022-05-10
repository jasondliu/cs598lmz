from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
print(s)
print(s.size)
# s.pack(10)

import struct
print(struct.pack(">I", 10))

print(struct.unpack(">I", b'\x00\x00\x00\x0a'))

print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))

# 格式化
# 大端法（big-endian）和小端法（little-endian）
# BMP格式采用小端法存储数据，文件头的结构按顺序如下：

# 两个字节：'BM'表示Windows位图，'BA'表示
