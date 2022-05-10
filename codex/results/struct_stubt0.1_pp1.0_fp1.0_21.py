from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# 可以使用format字符串来创建结构体
s = Struct('i')
s.size

# 使用pack方法将数据打包成字节字符串
s.pack(1)

# 使用unpack方法将字节字符串解包成原始数据
s.unpack(_)

# 可以使用iter_unpack方法将字节字符串解包成一个元组迭代器
s.iter_unpack(_ * 2)

# 可以使用pack_into方法将数据打包到一个可写的字节字
