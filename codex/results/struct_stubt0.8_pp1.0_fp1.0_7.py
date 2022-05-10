from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('!H')
s.size

s.unpack(b'\x01\x02')
s.pack(1)

s = Struct.__new__(Struct)
s.__init__('H')   # 十六进制，字节数为2
s.size

s.unpack(b'\x01\x02')
s.pack(1)

# struct的编解码运算符可以将多个元素打包或解包到命名元组中
from collections import namedtuple
Circle = namedtuple('Circle', ['x', 'y', 'r'])
c = Circle(1, 2, 3)
c.x, c.y, c.r

# 当然，你也可以直接传递一个字节
