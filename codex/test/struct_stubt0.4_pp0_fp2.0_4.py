from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack(b'\x00\x00\x00\x01')

# 可以用于构建不同类型的结构
s = Struct.__new__(Struct)
s.__init__('>I2sH')
s.unpack(b'\x00\x01\x00\x00abc\x00\x00')

# 使用类方法构建
Struct.__new__(Struct, '>I2sH')

# 使用类方法构建
Struct('>I2sH')

# 使用类方法构建
Struct(b'>I2sH')

