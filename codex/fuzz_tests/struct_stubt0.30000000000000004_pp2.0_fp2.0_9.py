from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

# 格式字符串的语法
# 格式字符串的语法和C语言类似，但是有一些不同之处：
#
# 字符串的第一个字符必须是一个大写字母，它表示字节顺序（Byte Order），可以是：
#
#     '>'：大端（Big-endian）字节顺序
#     '<'：小端（Little-endian）字节顺序
#     '='：与当前系统
