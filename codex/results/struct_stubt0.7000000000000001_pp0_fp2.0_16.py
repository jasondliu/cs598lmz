from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I 2s f'
s.size = s.calcsize(s.format)
print('format', s.format, 'size', s.size)
import struct
packed = struct.pack(s.format, 1, b'ab', 2.7)
print('contents:', binascii.hexlify(packed))
# unpack
print(struct.unpack(s.format, packed))

# 包含多个可变长度字段
record_struct = Struct('<idd')
print(record_struct.size)  # ->20

# 一种更简单的方法是使用字节对齐
record_struct = Struct('<idxxd')
print(record_struct.size)  # ->24

# 字节对齐的填充比计算固定大小要简单得
