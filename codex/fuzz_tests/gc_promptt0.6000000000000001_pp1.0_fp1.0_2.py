import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() on weakrefs

import gc

class C:
    pass

def f():
    o = C()
    r = weakref.ref(o)
    o.x = r

f()
gc.collect()

# This used to crash with a KeyError on o.x.

# This test verifies that all objects are collected when the weakref callback
# is called.

import weakref, gc

class C(object):
    pass

class D(object):
    def __init__(self):
        self.foo = C()
        self.ref = weakref.ref(self.foo, self.check)

    def check(self, wr):
        self.foo.bar = 42

d = D()
del d
gc.collect()

# Test that the callback is called with a dead weakref.

import weakref, gc

class C(object):
    def __init__(self):
        self.ref = weakref.ref(self, self.check)

    def check(self, wr):
        self
