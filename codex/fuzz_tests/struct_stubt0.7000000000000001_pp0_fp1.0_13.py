from _struct import Struct
s = Struct.__new__(Struct)
print s

class Point(object):
    __slots__ = ('x', 'y')

point = Point()
point.x = 1
point.y = 2
print point.x
print point.y
print point.__dict__

from abc import ABCMeta, abstractmethod
class A(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def spam(self, x):
        pass

a = A()

from abc import ABCMeta, abstractmethod
class A(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def spam(self, x):
        pass
try:
    a = A()
except TypeError:
    print 'error'

from abc import ABCMeta, abstractmethod
class A(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def spam(self, x):
        pass
class B(A):
    def spam(self, x):
        print x
b = B()
b.spam(2)

from ab
