import weakref
# Test weakref.ref() if class is a subclass of another class and
# the base class has a __del__ method.

from weakref import *
import gc

class B(object):
    def __init__(self, x=0):
        self.x = x
    def __del__(self):
        self.x = None

class C(B):
    def __init__(self, y=0):
        B.__init__(self, y)
        self.y = y

