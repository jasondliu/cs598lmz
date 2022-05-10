from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

# 可以使用类方法来创建结构体类
Struct.__new__(Struct, '>I')

# 创建一个结构体实例
s = Struct('>I')
s.pack(1)

# 创建一个结构体实例
s = Struct('>I')
s.pack(1)

# 创建一个结构体实例
s = Struct('>I')
s.pack(1)

# 创建一个结构体实例
s = Struct('>I')
s.pack(1)

# 创建一个结构体实例
s = Struct('>I')
