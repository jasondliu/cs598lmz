from _struct import Struct
s = Struct.__new__(Struct)
print(s)

# 创建结构体
s.__init__('i?f')
print(s)

# 将结构体打包
data = s.pack(1, False, 2.1)
print(data)

# 将结构体解包
print(s.unpack(data))

# 结构体的大小
print(s.size)
