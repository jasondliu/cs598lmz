from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# 其他方法
s = Struct('i')
s.pack(1)

# 可以把Struct对象看成一个类工厂

# 格式字符串
# 主要用于指定结构的字节对齐方式
# 如果没有指定对齐方式，默认是以最大字节数作为对齐
# 对齐方式：
# < 小端对齐
# > 大端对齐
# = 原始字节序
# ! 网络字节序

# 字
