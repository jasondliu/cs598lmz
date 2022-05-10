from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.size

# 打包
s.pack(1)

# 解包
s.unpack(b'\x00\x00\x00\x01')

# 打包和解包
s.pack_into(b'\x00\x00\x00\x01', 0, 1)
s.unpack_from(b'\x00\x00\x00\x01', 0)

# 字节序
s = Struct('>i')
s.pack(1)

s = Struct('<i')
s.pack(1)

# 使用结构体
import binascii

s = Struct('>I')
with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):
    start += 14
    fields = s.unpack_from(data, start)
   
