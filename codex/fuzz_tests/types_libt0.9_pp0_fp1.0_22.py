import types
types.SimpleNamespace()

from types import SimpleNamespace
SimpleNamespace()

from types import SimpleNamespace as SN
SN()
'''

################################################################################
# NamedTuples
from collections import namedtuple

Point = namedtuple('Point', 'x,y')
pt1 = Point(1.0, 5.0)
pt2 = Point(2.5, 1.5)

from math import hypot
line_length = hypot(pt1.x - pt2.x, pt1.y - pt2.y)
print(line_length)

print(pt1[0] + pt2[1])
x, y = pt1
print(x, y)

pt3 = Point._make([1.1, 2.2])
print(pt3)

print(pt1._asdict())
print({k: getattr(pt1, k) for k in pt1._fields})
t = [11, 22]
p = Point._make(t)
print(p)

print(Point(x=11, y=22))
print(
