import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() on weakrefs to objects with __del__ methods.

class C:
    def __init__(self, n):
        self.n = n
    def __del__(self):
        print "del", self.n

def f():
    c = C(1)
    wr = weakref.ref(c)
    c = C(2)
    gc.collect()
    print wr()
    c = C(3)
    gc.collect()
    print wr()
    c = C(4)
    gc.collect()
    print wr()
    c = C(5)
    gc.collect()
    print wr()

f()
