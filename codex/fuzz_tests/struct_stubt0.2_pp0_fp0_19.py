from _struct import Struct
s = Struct.__new__(Struct)
s.format = '>2s3s'
s.size = s.calcsize(s.format)
print(s.size)

# 实例化
s = Struct('>2s3s')
print(s.size)

# 将结构体打包成字节序列
data = s.pack('ab', b'\x00\x01', b'\x02\x03\x04')
print(data)

# 将字节序列解析成结构体
print(s.unpack(data))

# 将结构体解析成字典
print(s.unpack_from(data))

# 将字典打包成结构体
print(s.pack_into(data, 0, *(b'\x00\x01', b
