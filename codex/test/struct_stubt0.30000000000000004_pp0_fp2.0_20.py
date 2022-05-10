from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i?f')
s.size

# 字节序
# 无符号整数
# 有符号整数
# 浮点数

# 字节序标记
# @ 小端
# = 本地字节序
# < 小端
# > 大端
# ! 网络字节序

# 无符号整数
# B 1字节无符号整数
# H 2字节无符号整数
# I 4字节无符号整数
# Q 8字节无符号整数
# b 1字节有符号整数
# h 2字
