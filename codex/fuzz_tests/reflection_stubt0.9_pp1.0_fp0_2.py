fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__call__()
----------------
"""

"""
resolve the bug in this code

---------------------
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(A.__mro__)
print(D.__mro__)

------------------
"""

"""
class Ostrich:
    def __init__(self):
        self.__member = 0

    def __get__(self, obj, objtype):
        print('getting', self, obj, objtype, self.__member)

    def __set__(self, obj, val):
        print('setting', self, obj, val)
        self.__member = val

    def __delete__(self, obj):
        print('deleting', self, obj)
        del self.__member
"""

from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
