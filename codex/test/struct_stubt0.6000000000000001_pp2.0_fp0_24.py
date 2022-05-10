from _struct import Struct
s = Struct.__new__(Struct)
s.format = "I 2s f"
s.size = calcsize(s.format)
print(s.size)

# 这里创建一个字节数组
packed_data = pack(s.format, 1, b'ab', 2.7)
print(packed_data)

# 为什么要用Struct？
# 你可以使用Struct来处理二进制数据并将其解析为Python的数据类型。
# 一般来讲，你需要先从文件中读取二进制数据，然后使用unpack()方法将其转换为适当的数据类型。

# 创
