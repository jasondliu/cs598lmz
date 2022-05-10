from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

# 如果你想通过某个类创建实例，但是这个类的构造函数需要接受某些参数，那么你可以使用 functools.partial() 来固定这些参数
import math
from functools import partial
def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2 - x1, y2 - y1)
points = [(1, 2), (3, 4), (5, 6), (7, 8)]
pt = (4, 3)
points.sort(key=partial(distance, pt))
points

# 在回调函数中使用
