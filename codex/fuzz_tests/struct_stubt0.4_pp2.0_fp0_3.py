from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

# 也可以用下面的方式
from _struct import Struct
s = Struct('>I')
s.size

# 将结构体转换为字节字符串
from _struct import Struct
s = Struct('>I')
s.pack(12345)

# 将字节字符串转换为结构体
from _struct import Struct
s = Struct('>I')
s.unpack(b'\x00\x00\x30\x39')

# 将结构体转换为字节字符串
from _struct import Struct
s = Struct('>I')
s.pack(12345)

# 将字节字符串转
