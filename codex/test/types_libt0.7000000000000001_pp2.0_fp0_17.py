import types
types.SimpleNamespace(x=1, y=2)
 

from dataclasses import dataclass
@dataclass
class Point:
    x: int
    y: int
Point(1, 2)


from types import SimpleNamespace
Point = SimpleNamespace
Point(1, 2)
 

from dataclasses import dataclass
@dataclass
class Point:
    x: int
    y: int
Point(1, 2)
 

from collections import namedtuple
Point = namedtuple('Point', 'x y')
Point(1, 2)


from dataclasses import dataclass
@dataclass
class Point:
    x: int
    y: int
Point(1, 2)


from types import SimpleNamespace
Point = SimpleNamespace
Point(1, 2)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
Point(1, 2)
 

from dataclasses import dataclass
