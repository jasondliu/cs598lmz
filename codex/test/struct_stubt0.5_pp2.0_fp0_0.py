from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I 2s f'
s.size = s.calcsize()
print(s.size)

# 打开一个二进制文件
f = open('data.bin', 'wb')
data = s.pack(1, b'ab', 2.7)
print(data)
f.write(data)
f.close()

# 读取文件
f = open('data.bin', 'rb')
data = f.read()
print(data)
values = s.unpack(data)
