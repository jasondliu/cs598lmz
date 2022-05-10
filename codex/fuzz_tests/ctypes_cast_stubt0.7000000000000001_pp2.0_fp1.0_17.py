import ctypes
ctypes.cast(id(x), ctypes.py_object).value

print('\n\n####################################################################')
print('####################################################################')
print('####################################################################\n\n')

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({!r:}, {!r:})'.format(self.x, self.y)

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

class Circle(Point):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def __repr__(self):
        return 'Circle({!r:}, {!r:}, {!r:})'.format(self.x, self.y, self.radius)

    def __str__(self):
        return '({}, {}, {})'.format(self.x, self.y,
