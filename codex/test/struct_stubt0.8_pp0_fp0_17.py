from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I 2s f'
s.size = calcsize(s.format)

print(s.format)
print(s.size)

# 初始化
b = bytes(s.size)
print(b)

# 接收数据，初始化
# print(s.unpack(b))

# 给定文件名，
# 读取二进制数据，返回值
# 按照前面定义的 Struct 格式解包
# 使用 stdout 打印记录


# 定义结构：
# 二进制字符串格式
# 二进制字符串大小

# 使用 Struct
