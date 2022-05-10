from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

# 如果你想要通过某个类创建出实例来，但是这个类的构造函数需要接受某些参数，那么你可以使用 functools.partial() 来创建一个偏函数，然后使用它创建类的实例。
from functools import partial
Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)
p[0] + p[1]

x, y = p
x, y

p.x + p.y

p

# 如果你的程序中需要
