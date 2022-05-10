from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# 创建结构体实例
from _struct import Struct
s = Struct('i')
s.size

# 把结构体转换为字节字符串
from _struct import Struct
s = Struct('i')
s.pack(1)

# 把字节字符串转换为结构体
from _struct import Struct
s = Struct('i')
s.unpack(b'\x00\x00\x00\x01')

# 使用结构体解析二进制数据
from _struct import Struct
import binascii

s = Struct('>I 2s f')
packed_data = s.pack(12345, b'ab', 1.23)
