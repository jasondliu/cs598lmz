from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I 2s f'
s.size = s.calcsize()
print(s.size)

# 实例化Struct对象
s = Struct('I 2s f')
print(s.size)

# pack的第一个参数是一个可迭代对象，但是*可以把一个可迭代对象拆开作为函数的参数
values = (1, b'ab', 2.7)
print(s.pack(*values))

# unpack把bytes变成一个元组，与之对应的是pack把元组变成bytes
print(s.unpack(b'\x01\x00\x00\x00ab\x00\x00\x00\x00\x00\x00\xcd@'))


