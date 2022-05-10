import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() on objects which have __del__ methods.

import gc

class A(object):
    def __init__(self, n):
        self.n = n
    def __del__(self):
        self.n = None
        print "deleting A"

class B(object):
    def __init__(self, n):
        self.n = n
    def __del__(self):
        global a
        a.n = 0
        print "deleting B"

class C(object):
    def __init__(self, n):
        self.n = n
    def __del__(self):
        print "deleting C"

for i in xrange(1, 10):
    a = A(i)
    b = B(i)
    c = C(i)
    gc.collect()
    print "collecting (%d)." % i

# This test used to segfault because of a reference cycle between the
# __del__ method of class B and the local "a" variable.

# Should
