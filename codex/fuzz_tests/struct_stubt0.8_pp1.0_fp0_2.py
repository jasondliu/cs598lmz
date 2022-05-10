from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i2shi')
s.size
s.pack(1, b'xy', 2, b'z')
s.unpack(_)
s.unpack_from(b'\x01\x00\x00\x00xy\x02\x00\x00\x00z', 0)

import sys
sys.getsizeof(1)
import array
sys.getsizeof(array.array('c', 'x' * 1000))

>>> class Point:
...     __slots__ = ['x', 'y']
...     def __init__(self, x, y):
...         self.x = x
...         self.y = y
...     def __repr__(self):
...         return 'Point({!r:},{!r:})'.format(self.x, self.y)
... 
>>> p = Point(1, 2)
>>> p
Point(1,2)

>>> class Point:
...     __slots__ = ['x', 'y']
...     def __init__(self, x
