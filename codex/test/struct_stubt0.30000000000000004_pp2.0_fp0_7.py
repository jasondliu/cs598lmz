from _struct import Struct
s = Struct.__new__(Struct)
s.format = '>I'
s.size = 4
print(s.unpack(b'\x00\x00\x00\x00'))
print(s.unpack(b'\x00\x00\x00\x01'))
print(s.unpack(b'\x00\x00\x01\x00'))
print(s.unpack(b'\x00\x01\x00\x00'))
print(s.unpack(b'\x01\x00\x00\x00'))

# 如果你想构造一个类似的结构，但是又不想定义一个新的类，可以使用 namedtuple() 函数。
# 这个函数实际上是一个返回 Python 中标准元组类型
