from _struct import Struct
s = Struct.__new__(Struct)
s.__init__(">i")
print(s.size)
print(s.pack(1))

# 使用format字符串来表示具体的格式
# format字符串可以使用的字符：
# 字符	含义
# @	被格式化的对象将会被传递给str()函数然后输出
# =	字段宽度会被设置为右对齐，而不是左对齐
# <	输出的字段将会被左对齐
# ^	输出的字段将会被居中对齐
# >	输
