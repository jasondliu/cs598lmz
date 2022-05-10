import types
types.SimpleNamespace(x=1, y=2)

#   - создать экземпляр класса
import random
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'({self.x}, {self.y})'
    def __str__(self):
        return 'My Point'

points = []
for _ in range(10):
    points.append(Point(random.randint(0, 15), random.randint(0, 15)))

#   - создать список (list)
import random

l = [random.randint(0, 15) for _ in range(10)]
print(l)

#   - создать кортеж (tuple)
import random

t = tuple(random.randint(0, 15
