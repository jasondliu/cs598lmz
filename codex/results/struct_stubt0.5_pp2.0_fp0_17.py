from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'hhl'
s.size = 8

print(s.unpack(b'\x01\x02\x03\x04\x05\x06\x07\x08'))

# 如果你要创建大量的结构体实例，可以预先编译他们。
# 下面是一个小例子，演示了如何使用一个元组存储编译后的结构体类：

from timeit import timeit
Point = namedtuple('Point', ['x', 'y'])
# print(timeit('Point(1, 2)', 'from __main__ import Point', number=1000000))
# print(timeit('dict(x=1, y=2)', 'from __main__ import Point
