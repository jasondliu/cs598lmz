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

def check(b):
    if not b.x is None:
        raise ValueError, "b.x still reachable"

def check_c(c):
    if not c.x is None:
        raise ValueError, "c.x still reachable"
    if not c.y is None:
        raise ValueError, "c.y still reachable"

def check_subclass(sub, base):
    if not issubclass(sub, base):
        raise ValueError, "%s is not a subclass of %s"%(sub,base)

check_subclass
