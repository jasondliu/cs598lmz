from _struct import Struct
s = Struct.__new__(Struct)
print(len(s))

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, tuple):
            return self.x * other[0] + self.y * other[1]
        elif isinstance(other, Point):
            return self.x * other.x + self.y * other.y
        else:
            return self

    def __matmul__(self, other):
        if isinstance(other, tuple):
            return self.x * other[0] + self.y * other[1]
        else:
            return self

