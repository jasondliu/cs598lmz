from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.size

# 使用struct模块来解析二进制
s = Struct('>i')
s.unpack(b'\x00\x00\x00\x01')

# 将数据打包成二进制
s.pack(1)

# 将数据打包成二进制，并写入文件
with open('data.bin', 'wb') as f:
    f.write(s.pack(1))

# 从文件中读取二进制数据
with open('data.bin', 'rb') as f:
    data = f.read()
    print(s.unpack(data))

# 将多个数据打包成二进制
s = Struct('>
