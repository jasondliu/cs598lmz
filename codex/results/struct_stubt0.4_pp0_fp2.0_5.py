from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('L')
s.size

# 可以使用format字符串指定结构的格式
# 格式字符串中的每个字母都表示一个C结构中的成员
# 字母后面的数字表示该成员的长度
# 使用结构时，需要将其序列化为字节字符串
# 可以使用pack()方法将结构转换为字节字符串
# 也可以使用unpack()方法将字节字符串转
