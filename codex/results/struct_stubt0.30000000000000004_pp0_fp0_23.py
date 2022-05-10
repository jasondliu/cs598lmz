from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

class Point(object):
    __slots__ = ['x', 'y']

p = Point()
p.x = 1
p.y = 2
p.z = 3

class Point(object):
    __slots__ = ['x', 'y']
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(1, 2)
p.x
p.y
p.z

class Point(object):
    __slots__ = ['x', 'y']
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Point(%d, %d)' % (self.x, self.y)

p = Point(1, 2)
p

class Point(object):
    __slots__ = ['x', 'y']
    def __init__(self, x, y):
        self.x
