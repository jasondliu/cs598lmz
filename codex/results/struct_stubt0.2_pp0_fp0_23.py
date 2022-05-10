from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I 2s f'
s.size = s.calcsize(s.format)
print(s.size)

# 实例化Struct对象
s = Struct('I 2s f')
print(s.size)

# 将结构体转换为字节流
values = (1, b'ab', 2.7)
print(s.pack(*values))

# 将字节流转换为结构体
print(s.unpack(b'\x01ab\x00\x00\x00\x00\x00\x00\xcd@'))

# 将字节流转换为结构体
with open('data.b', 'rb') as f:
    data = f.read()
    print(s.unpack(data))

# 将
