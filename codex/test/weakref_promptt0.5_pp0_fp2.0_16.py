import weakref
# Test weakref.ref() and weakref.proxy()

from test import support
from test.support import verbose, TestFailed

class C(object):
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return "<C instance at %d>" % id(self)

class D(object):
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return "<D instance at %d>" % id(self)

class E(object):
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return "<E instance at %d>" % id(self)

def f():
    return "hello"

def g():
    return "hello"

def h():
    return "hello"

def show_refs(r1, r2, r3):
    print("r1 =", r1, "   refcount =", sys.getrefcount(r1))
