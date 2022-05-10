from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I 2s f'
s.size = s.calcsize(s.format)
print(s.size)

# 给出一个结构体实例，可以通过调用实例的 pack() 方法将其打包为一个字节字符串
print(s.pack(1, b'ab', 2.7))

# 解压时，使用 unpack() 方法，传入相同的格式字符串
print(s.unpack(b'\x01\x00\x00\x00ab\x00\x00\x00\x00\x00\x00(B'))

# 如果需要将结构体打包到一个文件
