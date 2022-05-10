from _struct import Struct
s = Struct.__new__(Struct)
prefix = '>'
filler = '@'
filler = ''
filler = '!'
filler = '<'
s.format = prefix + 'HHHH'
s.size = s.calcsize(s.format)
h2d = 0
h2d = 1
class Point(object):
    __slots__= ('x', 'y');
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return self.__class__.__name__ + '(%s, %s)' % (self.x, self.y)

pts = []
for i in range(10):
    pt = Point(*divmod(i, 5))
