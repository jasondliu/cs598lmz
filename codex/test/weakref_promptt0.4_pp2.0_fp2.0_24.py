import weakref
# Test weakref.ref() for callable objects.
import sys
import pickle
import gc
import operator
import unittest
import test.support
from test.support import captured_stdout

# This is a callable object.
class C:
    def __call__(self):
        pass

class D:
    def __init__(self, x):
        self.x = x
    def __call__(self):
        return self.x

class E:
    def __init__(self, x):
        self.x = x
    def __call__(self, y):
        return self.x + y

class F:
    def __init__(self, x):
        self.x = x
    def __call__(self, y, z=1):
        return self.x + y + z

class G:
    def __init__(self, x):
        self.x = x
    def __call__(self, y, *z):
        return self.x + y + sum(z)

