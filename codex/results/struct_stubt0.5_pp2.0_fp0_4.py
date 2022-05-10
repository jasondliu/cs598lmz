from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i?f')
s.size

# 每个实例都有一个pack方法和一个unpack方法，可以用来执行打包和解包操作
s.pack(1, False, 3.14)
s.unpack(_)

# 可以使用可选参数endianness和size来控制Struct的行为
s = Struct('>i?f')
s.pack(1, False, 3.14)
s.unpack(_)

# 可以使用格式说明符来调整字节对齐
s = Struct('i?f')
s.size
s = Struct('i?xf')
s.size

# 可以使用格式说明
