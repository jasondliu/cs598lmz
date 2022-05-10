from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.size

# 注意：
# Struct.__new__() 接受的第一个参数是格式字符串，而不是类名。
# 因此，使用 __new__() 创建结构体类时，不能提供类名。为了解决这个问题，
# 可以使用 lambda 表达式来创建一个简单的匿名结构体类。

def make_struct(format):
    return Struct(format)

# 创建一个简单的匿名结构体类

Point = make_
