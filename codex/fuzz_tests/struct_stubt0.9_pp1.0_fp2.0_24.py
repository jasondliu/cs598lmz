from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("i")
s.size

s = Struct("i")
s.size

s = Struct("i")
s.pack(1)   # 指定数字参数后，打包成二进制数据

s.unpack(_)   # 解包成相应的值

# 将数字转化为二进制编码
# bin(s) 函数可以将数字转化为二进制，并且是ASCII 码形式
bin(4)

int(b'0b11', 0)   # 转化为10进制
