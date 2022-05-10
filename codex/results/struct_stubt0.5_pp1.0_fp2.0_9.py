from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I 2s f'
s.size = calcsize(s.format)
print(s.size)

# _struct.Struct.__new__() 不能直接调用，需要传入format参数
# 下面的操作是错误的
# s = Struct.__new__()
# s.format = 'I 2s f'
# s.size = calcsize(s.format)
# print(s.size)

# 生成一个结构体对象
s = Struct('I 2s f')
print(s.size)

# 将一个结构体对象转换为二进制的bytes
packed_data = s.pack(1, b'ab', 2.7)
print(packed_data)

# 将一个二
