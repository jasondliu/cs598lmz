from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
print(s.size)

# 从字节序列解析出结构
print(s.unpack(b'\x00\x00\x00\x01'))

# 将结构打包为字节序列
print(s.pack(1))

# 使用struct模块来解决字节序列和Python值之间转换的问题
# 可以使用标准的struct模块创建自定义的格式化程序
# 在struct模块中定义的格式化程序可以用来处理网络数
