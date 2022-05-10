from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i?f')
s.size

# 使用pack函数打包
s.pack(1, False, 3.14)

# 使用unpack函数解包
s.unpack(_)

# 使用iter_unpack函数迭代解包
