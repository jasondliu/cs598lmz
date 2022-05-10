from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
print(s.size)
print(s.pack(1))
print(s.unpack(s.pack(1)))

# 创建一个结构体类
from _struct import Struct
s = Struct('i?f')
print(s.size)
print(s.pack(1, False, 2.3))
print(s.unpack(s.pack(1, False, 2.3)))

# 创建一个结构体类
from _struct import Struct
s = Struct('i?f')
print(s.size)
print(s.pack(1, False, 2.3))
print(s.unpack(s.pack(1, False, 2.3)))

# 创建一个结构体类
from _struct import Struct
s = Struct('i?f')
print(s.size)
print(s.pack(1, False,
