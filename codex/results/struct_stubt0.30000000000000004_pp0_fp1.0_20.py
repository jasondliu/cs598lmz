from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
print(s.size)

# 可以用一个元组来初始化一个结构体
s = Struct('i')
print(s.size)

# 可以用一个字节序列来初始化一个结构体
s = Struct(b'>i')
print(s.size)

# 可以用一个字节序列来初始化一个结构体
s = Struct('>i')
print(s.size)

# 可以用一个字节序列来初始化一个结构体
s = Struct('i')
print(s.size)

# 可以用一个字节序
