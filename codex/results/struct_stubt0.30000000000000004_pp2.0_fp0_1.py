from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# 使用类方法
Struct.__new__(Struct, 'i')

# 使用类方法
Struct('i')

# 使用类方法
Struct('i').size

# 使用类方法
Struct('i').pack(1)

# 使用类方法
Struct('i').unpack(b'\x01\x00\x00\x00')

# 使用类方法
Struct('i').unpack_from(b'\x01\x00\x00\x00', 0)

# 使用类方法
Struct('i').unpack_from(b'\x01\x00\x00\x00', 0)[0]

# 使用类方法
Struct('i').unpack_from(b'\x01\x00\x00\x00', 0)[
