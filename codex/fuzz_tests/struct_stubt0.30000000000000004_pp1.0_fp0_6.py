from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

# 使用struct模块将Python的数据类型转换为字节
s.pack(1)

# 使用struct模块将字节转换为Python的数据类型
s.unpack(b'\x00\x00\x00\x01')

# 把一个结构体变成一个字节字符串
s = Struct('>I 2s f')
values = (1, 'ab'.encode('utf-8'), 2.7)
s.pack(*values)

# 把一个字节字符串解压为一个结构体
s.unpack(b'\x00\x00\x00\
