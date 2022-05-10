from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

# 可以使用格式字符串将结构体打包为字节字符串
s.pack(1)

# 可以使用格式字符串将字节字符串解包为结构体
s.unpack(_)

# 可以使用格式字符串计算结构体的大小
s.size

# 可以使用格式字符串计算结构体的大小
s.pack_into(b'abcdef', 1, 2)

