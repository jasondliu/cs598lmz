import types
types.MethodType(c.__mul__, None)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Point({!r:},{!r:})'.format(self.x, self.y)

import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def __repr__(self):
        return 'Circle({})'.format(self.radius)
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius
    def __add__(self, other):
        return Circle(self.radius + other.radius)
    def __mul__(self, other):
        return Circle(self.radius * other)
    def __rmul__(self, other):
        return Circle(self.radius * other)
    def __gt__(self, other):
        return self.
