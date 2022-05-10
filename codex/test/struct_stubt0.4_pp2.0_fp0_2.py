from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i?f')
s.pack(1, False, 3.14)

# 使用struct模块的pack函数打包，使用unpack函数解包。
# pack的第一个参数是一个格式字符串，格式字符串里面的每个字母代表了一种C语言的原生类型，比如i代表int，f代表float。

# 实际上，这种类型就是Python3的int和float类型，所以你不需要特别地对它们做转换。
# 后
