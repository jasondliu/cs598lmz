from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack(b'\x01\x00\x00\x00')

# 使用给定的格式将给定的字节字符串解压缩为一个元组。
# 如果提供了可选的字节序列，则使用它来解释字节字符串。
# 否则，使用默认的字节序列，它是小端序（小端字节序）。
# 如果字节字符串的长度不是格式的整数倍，则会引发
