import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() on weakrefs to objects with __del__ methods

class C:
    def __init__(self):
        self.a = self.b = self.c = self.d = None
    def __del__(self):
        pass

def f():
    c = C()
    c.a = c.b = c.c = c.d = c
    wr = weakref.ref(c)
    del c
    return wr

w = f()
gc.collect()
print w() is None
