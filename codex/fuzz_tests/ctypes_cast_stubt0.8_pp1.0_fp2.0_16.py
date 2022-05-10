import ctypes
ctypes.cast(id(int), ctypes.py_object).value

import sys
sys.getrefcount(1)

a = [1, 2, 3]
b = [4, 5, 6]
a.append(b)
b.append(a)

a = None

import gc
gc.collect()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x}, {self.y})'


a = Point(23, 42)
b = Point(50, -7)
a.another = b
b.another = a

import sys
sys.getrefcount(a)

b = None

import gc
gc.collect()

a.x = None
b = a.another
a = None
b = None

import gc
gc.collect()

a = None
b = None
gc.collect()

a = None
b = None
gc.collect()


