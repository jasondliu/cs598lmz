from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.unpack(b'\x00\x00\x00\x01')

# 实例化Struct对象
s = Struct('>i')
s.unpack(b'\x00\x00\x00\x01')

# 将字节流转换成元组
s.unpack_from(b'\x00\x00\x00\x01\x00\x00\x00\x02', 4)

# 将元组转换成字节流
s.pack(1, 2)

# 将元组转换成字节流，并将字节流写入文件
with open('data.bin', 'wb') as f:
    f.write(s.pack(1, 2))

#
