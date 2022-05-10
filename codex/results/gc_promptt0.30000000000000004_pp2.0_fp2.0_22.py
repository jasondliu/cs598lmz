import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs to objects that have __del__ methods

class A:
    def __del__(self):
        pass

def f():
    a = A()
    wr = weakref.ref(a)
    del a
    gc.collect()
    return wr

wr = f()
print wr()
del f
gc.collect()
print wr()
