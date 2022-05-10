from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<h')
print(s.size)
print(s.pack(42))
print(s.unpack(s.pack(42)))

# 定义一个类，它的实例能存储坐标
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2, 3)
print(p.x, p.y)

# 定义一个类，它的实例能存储坐标，但是坐标是可以变化的
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'Point({self.x}, {self.y})'
    def __str__(self):
        return
