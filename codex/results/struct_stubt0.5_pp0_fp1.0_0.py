from _struct import Struct
s = Struct.__new__(Struct)
s.__init__()
s.format = 'I 2s f'
s.size = s.calcsize(s.format)
print(s.size)

# 使用
import struct

packed_data = struct.pack('>i4sh', 7, b'spam', 8)
print(packed_data)

data = struct.unpack('>i4sh', packed_data)
print(data)

# 将元组转化为字节
print(struct.pack('>i4sh', *data))

# 字节转化为元组
print(struct.unpack('>i4sh', b'\x00\x00\x00\x07spam\x00\x08'))

# 使用file对象
with open('data.bin', 'wb') as f:
    f.write(struct.pack('>i4sh', 7, b'spam', 8))

with open
