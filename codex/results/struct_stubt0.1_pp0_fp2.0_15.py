from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I 2s f'
s.size = s.calcsize()
print(s.size)

# 可以使用unpack方法从字节字符串中读取信息
data = b'\x00\x00\x00\x07spam\x00\x08\x00\x00\x00'
print(s.unpack(data))

# 可以使用pack方法将Python值打包进字节字符串中
print(s.pack(7, b'spam', 3.0))

# 可以使用iter_unpack方法从字节字符串中读取信息
data = b'\x00\x00\x00\x07spam\x00\x08\x00\x00\x00\x00\x00\x
