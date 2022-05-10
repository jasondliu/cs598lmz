from _struct import Struct
s = Struct.__new__(Struct)
s.format = '@2s10s'
s.size = s.calcsize(s.format)
s.pack('xx')

# 使用pack()方法时，字符串的长度必须和规定的一致。
# 如果给定的字符串太长了，则会截断它。
# 如果给定的字符串太短了，则会在后面填充空字节。

data = s.pack('xx')
len(data)
data
data = s.pack('AB')
len(data)
data
data = s.pack('A12')
len(data)
data

# 如果你想从结构中
