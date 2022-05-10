from _struct import Struct
s = Struct.__new__(Struct)
s.format = '>2s2s'
s.size = s.calcsize(s.format)
print(s.size)

# 下面的程序实现了一个简单的结构体，它的作用是将一个整数转换成二进制数组
# 它的第一个字节是整数的高8位，第二个字节是整数的低8位

