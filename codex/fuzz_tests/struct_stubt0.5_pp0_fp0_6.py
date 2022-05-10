from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I 2s f'
s.size = s.calcsize()

print(s.size)
print(s.pack(1, b'ab', 2.7))
print(s.unpack(b'\x01\x00\x00\x00ab\x00\x00\x9a\x99\x99\x99\x99\x99\xf1?'))

# 使用struct模块处理二进制数据时，大多数struct函数都有一个标志位参数，用来控制字节顺序、
# 数据对齐等。尽管在大多数情况下，默认值就能满足需求，但是在
