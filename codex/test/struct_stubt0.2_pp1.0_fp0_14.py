from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.pack(1)

# 打包的数据都是字节字符串
# 可以使用标准的bytes函数将其转换为字节字符串
numbers = (1, 2, 3)
s.pack_into(buffer, 0, *numbers)

# 可以使用标准的bytes函数将其转换为字节字符串
# 可以使用标准的bytes函数将其转换为字节字符串
# 可以使用标准的bytes函数将其转换为字节字符串
# 可以使用
