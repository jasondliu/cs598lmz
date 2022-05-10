import weakref
# Test weakref.ref()
import gc
import operator
import sys
import traceback
import unittest
from test import support
import types
import _weakref

# Test creation of weak references to methods
class C:
    def f(self, arg=123):
        pass

# Test creation of weak references to callable objects
class C2:
    def __call__(self):
        pass

class MyTuple(tuple):
    pass

class MyList(list):
    pass

class MyDict(dict):
    pass

class MyInt(int):
    pass

class MyLong(int):
    pass

class MyFloat(float):
    pass

class MyStr(str):
    pass

class MyUnicode(str):
    pass

class MyObject:
    pass

class MyException(Exception):
    pass

def f(*args, **kw):
    pass

def f2(*args, **kw):
    raise MyException

def f3(a, b, c):
    return a, b, c

