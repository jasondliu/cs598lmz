import weakref
# Test weakref.ref() for objects with a destructor.
import gc
import sys

class C:
    def __init__(self):
        self.x = 1
    def __del__(self):
        print 'del'

def f():
    return C()

for i in xrange(8):
    r = weakref.ref(f())
    if r() is None:
        raise RuntimeError
    gc.collect()

for i in xrange(8):
    r = weakref.ref(C())
    if r() is None:
        raise RuntimeError
    gc.collect()

for i in xrange(8):
    r = weakref.ref(C())
    del r
    gc.collect()

# Check that different weakrefs can point to objects with the same
# custom __hash__() implementation.

class H:
    def __hash__(self):
        return 1

w1 = weakref.ref(H())
w2 = weakref.ref(H())

# Check that weakref.ref() doesn't call __
