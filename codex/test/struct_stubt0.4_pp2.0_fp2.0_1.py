from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<h')
s.pack(1)
print(s.size)
print(s.pack(1))
print(s.unpack(s.pack(1)))

# 创建一个结构体对象
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<h')
print(s.size)
print(s.pack(1))
print(s.unpack(s.pack(1)))

# 创建一个结构体对象
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<h')
print(s.size)
print(s.pack(1))
print(s.unpack(s.pack(1)))

# 创建一个结构体对象
from _struct import Struct
s = Struct.__new__(Struct)
s
