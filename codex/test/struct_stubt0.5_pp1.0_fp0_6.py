from _struct import Struct
s = Struct.__new__(Struct)
s.pack('>hhl',1,2,3)

# 为了构建一个新的结构体类，使用format字符串将各种格式组合起来，然后使用类名和format字符串作为参数调用Struct

# 如果你想将某个格式作为元组的元素，那么你需要在它前面加上一个括号，这样struct才会理解你的意图

s = Struct('i?f')
s.pack(1,False,2.7)

# 可以使用unpack方法将bytes
