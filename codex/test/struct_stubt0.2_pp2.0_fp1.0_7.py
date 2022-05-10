from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack(b'\x01\x00\x00\x00')

# 将结构体转换成字节流
s = Struct('i')
s.pack(1)

# 将字节流转换成结构体
s = Struct('i')
s.unpack(b'\x01\x00\x00\x00')

# 将结构体转换成字节流
s = Struct('i')
s.pack(1)

# 将字节流转换成结构体
s = Struct('i')
s.unpack(b'\x01\x00\x00\x00')

# 将结构体转换成字
