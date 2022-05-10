from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

# _struct.Struct.unpack(s, b'\x12\x34\x56\x78abcd')
# (305419896, b'ab', 2.700000047683716)

import struct
struct.pack('>I', 10240099)
# b'\x00\x9c@c'
struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
# (4042322160, 32896)

# struct模块实现了在Python字符串和C struct之间转换的函数。
# 主要用于二进制数据的操作。

# 在Python中，比方说要把一个32位无符号整数变
