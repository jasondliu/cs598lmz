import types
types.SimpleNamespace

# 这里是将一个字典转化为一个类对象
class Obj(object):
    pass
a = {'a': 1, 'b': 2, 'c': 3}
o = Obj()
for key, value in a.items():
    setattr(o, key, value)
print(o.a, o.b, o.c)


# 使用collections.namedtuple
from collections import namedtuple
Point = namedtuple('Point', 'x y z')
p = Point(1, 2, 3)
print(p.x, p.y, p.z)

# 使用types.SimpleNamespace
from types import SimpleNamespace
Point = SimpleNamespace(x=1, y=2, z=3)
print(Point.x, Point.y, Point.z)

# 使用字典
a = {'x': 1, 'y': 2, 'z': 3}
