from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'i'
s.size = 4
s.pack(1)

# 可以通过给Struct实例设置format属性来改变它的解析规则。
# 下面的例子演示了如何将一个4字节的整数转换成一个浮点数：
from _struct import Struct
f = Struct('i').unpack(b'\x00\x00\x00\x00')
f

# 如果你想将C结构体转换成Python字典，你可以很容易的定义一个转换函数：
