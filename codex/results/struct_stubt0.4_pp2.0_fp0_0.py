from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<h')
print(s.size)
print(s.pack(1))
print(s.unpack(s.pack(1)))

# 打印结果：
# 2
# b'\x01\x00'
# (1,)

# 创建一个结构类型，这个结构类型可以按照指定的格式打包和解包
# 可以看到，结构类型中包含了一个格式字符串，用来指定结构的类型和大小
# 另外，结构类型还包
