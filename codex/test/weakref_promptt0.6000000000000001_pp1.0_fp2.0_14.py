import weakref
# Test weakref.ref and weakref.proxy with objects implementing __slots__.
import unittest
from test import test_support
from weakref import ref, proxy
from types import ClassType
from UserList import UserList
from UserDict import UserDict
from UserString import UserString
from collections import deque

class Foo(object):
    __slots__ = ['a', 'b']

class Bar(Foo):
    __slots__ = ['c', 'd']

class Foo2(object):
    __slots__ = ['a', 'b']
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Bar2(Foo2):
    __slots__ = ['c', 'd']
    def __init__(self, a, b, c, d):
        Foo2.__init__(self, a, b)
        self.c = c
        self.d = d

class Foo3(object):
    __slots__ = ['a', 'b', '__dict__']

