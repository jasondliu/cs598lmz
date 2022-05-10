import ctypes
ctypes.cast(l, ctypes.py_object).value

l.value

#anonymous tuples
t = (1, 2, 3)
t

#a list that is contained in a tuple
t = (1, [2, 3, 4], 5)
t[1].append(5)
t

#formatting long ints
num = 2398129381923
f'{num:,}'


class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

p = Point3D(1, 2, 3)
p.x
p.y
p.z


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'Point({self.x}, {self.y})'


p = Point(1, 2)
p

print(p)

str(Point(1, 2))

#
