from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I 2s f'
s.size = s.calcsize()
print(s.size)

import binascii
packed_data = s.pack(1, b'ab', 2.7)
print(packed_data)
print(binascii.hexlify(packed_data))

data = s.unpack(packed_data)
print(data)

# 如果需要更复杂的编码，可以使用struct模块中的更高级函数
# 函数pack_into()和unpack_from()允许你在一个已存在的字节缓冲区中执行数据的编码和解码操作
import struct
import binascii

