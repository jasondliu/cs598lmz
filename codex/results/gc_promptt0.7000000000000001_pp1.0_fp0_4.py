import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() handling of weakrefs to self
class A:
    def __init__(self, i):
        self.i = i
        self.ref = weakref.ref(self)

import sys
a = A(1)
a.x = a
sys.getrefcount(a)
a = None
gc.collect()

# Test gc.collect() handling of weakrefs to self
class A:
    def __init__(self, i):
        self.i = i
        self.ref = weakref.ref(self)

import sys
a = A(1)
a.x = a
sys.getrefcount(a)
a = None
gc.collect()

# Test gc.collect() handling of weakrefs to cyclic data structures
class A:
    pass

a = A()
b = A()
a.x = b
b.x = a
a.x.x.x.x = a
a = None
b = None
gc.collect()

# Test gc.collect() handling of weakrefs to cyclic
