from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('iif')
print(s.size)
print(s.pack(1, 2, 3.0))
print(s.unpack(b'\x01\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00'))
print(s.unpack_from(b'\x01\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00', 4))

class Point(object):
    __slots__ = ['x', 'y']
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(1, 2)
print(hasattr(p, '__dict__'))
print(dir(p))

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(1, 2)
print
