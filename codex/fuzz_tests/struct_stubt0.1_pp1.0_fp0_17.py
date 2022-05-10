from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

# 可以使用格式字符串将结构体对象转换为字节字符串
s.pack(1)

# 可以使用格式字符串将字节字符串转换为结构体对象
s.unpack(b'\x00\x00\x00\x01')

# 可以使用格式字符串将结构体对象转换为字节字符串
s.pack_into(b'\x00\x00\x00\x00', 0, 1)

# 可以使用格式字
