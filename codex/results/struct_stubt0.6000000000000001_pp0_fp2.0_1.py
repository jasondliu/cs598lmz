from _struct import Struct
s = Struct.__new__(Struct)
s.pack('>i', 10240099)

# '>i'表示使用大端法读取一个整数

# pack的第一个参数是处理指令，'>i'的意思是：
# >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。

# 后面的参数个数要和处理指令一致。

# unpack把bytes变成相应的数据类型：

>>> s.unpack('>i', b'\x00\x9c@c')
(10240099,)

# 根
