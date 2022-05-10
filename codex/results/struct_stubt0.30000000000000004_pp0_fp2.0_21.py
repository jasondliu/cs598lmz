from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack(b'\x01\x00\x00\x00')

# 或者
from _struct import Struct
s = Struct('i')
s.unpack(b'\x01\x00\x00\x00')

# 为了更加方便的处理，可以使用更高级的模块struct
from struct import Struct
s = Struct('i')
s.unpack(b'\x01\x00\x00\x00')

# 可以使用一个字节对齐的方式来处理字节字符串
from struct import Struct
s = Struct('>i')
s.unpack(b'\x00\x00\x00\x01')

# 可以使用一个字节对
