from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i?f')
s.size

# Exporting a class

class Point:
    __slots__ = ('x', 'y')

Point = make_dataclass('Point', 'x y')

# Using a class

p = Point(2, 3)
p

p.x

p.x = 4

# Using a class

p = Point(2, 3)

import math

def distance(p1, p2):
    return math.hypot(p1.x - p2.x, p1.y - p2.y)

distance(p, Point(0, 0))

# Using a class

Point(2, 3) == Point(2, 4)

Point(2, 3) == Point(3, 2)

Point(2, 3) == (2, 3)

# Using a class

p1 = Point(2, 3)
p2 = Point(2, 3)

p1 == p2

p1 is p2

# Using a class

