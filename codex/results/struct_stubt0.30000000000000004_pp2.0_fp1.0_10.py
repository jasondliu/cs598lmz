from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.size

# 创建一个空的结构体
s = Struct.__new__(Struct)
s.__init__('>i')
s.pack(1)

# 使用结构体的pack方法将数据打包成字节
s = Struct('>i')
s.pack(1)

# 使用结构体的unpack方法将字节解包成数据
s = Struct('>i')
s.unpack(b'\x00\x00\x00\x01')

# 使用结构体的unpack_from方法从字节流中解包
s = Struct('>i')
s.unpack_from(b'\x00\x00\x00\x01\
