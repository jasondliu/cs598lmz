import types
types.SimpleNamespace # Python >= 3.3
#types.Namespace # Python <= 3.2

import collections
collections.namedtuple(
    'Point', 
    ['x', 'y']
)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Point:
    __slots__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Point:
    __slots__ = ('__x', '__y') # private
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('x must be int or float')
        self.__x = value
