from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<3s3sHH'
print(s.size)

# 可以使用格式字符串 '>6s9s5s' 创建一个新的 struct 实例
s = Struct('>6s9s5s')
print(s.size)

# 格式字符串 '<' 代表小端法存储， '>' 代表大端法存储
# '6s' 表示 6 个字节的字符串
# '9s' 表示 9 个字节的字符串
# '5s' 表示 5 个字节的字符串
# 合起来，就是一个 20 个字节
