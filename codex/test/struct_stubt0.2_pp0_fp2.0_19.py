from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# 不能直接实例化，需要使用__new__方法
# s = Struct('i')
# s.pack(1)

# 可以使用类方法
Struct.pack('i', 1)

# 可以使用类方法
Struct.unpack('i', b'\x00\x00\x00\x01')

# 可以使用类方法
Struct.calcsize('i')

# 可以使用类方法
Struct.unpack_from('i', b'\x00\x00\x00\x01')

# 可以使用类方法
Struct.pack_into('i', b'\x00'*4, 0, 1)

# 可以使用类
