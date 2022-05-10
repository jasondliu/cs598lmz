from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I')
s.unpack(b'\x00\x00\x00\x00')

# 使用字节码对象
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__(b'I')
s.unpack(b'\x00\x00\x00\x00')

# 使用字符串
from _struct import Struct
s = Struct(b'I')
s.unpack(b'\x00\x00\x00\x00')

# 使用字符串
from _struct import Struct
s = Struct('I')
s.unpack(b'\x00\x00\x00\x00')

# 使用字符串
from _struct import Struct
s = Struct('I')
s.unpack_from(b'\x00\x00\x00\x00', 0)

# 使
