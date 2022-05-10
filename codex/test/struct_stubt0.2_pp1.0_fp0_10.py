from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I 2s f'
s.size = s.calcsize()
print(s.size)

# 创建一个结构体对象
import struct
st = struct.Struct('I 2s f')
print(st.size)

# 将结构体打包成字节串
values = (1, 'ab'.encode('utf-8'), 2.7)
print(st.pack(*values))

# 将字节串解包成结构体
print(st.unpack(b'\x01\x00\x00\x00ab\x00\x00\x00\x00\x00\x00\xcd@'))

# 将结构体打包成字节串
print(st.pack_into(values, 0))

# 将字
