import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs

class A:
    pass

a = A()
wr = weakref.ref(a)

gc.collect()
gc.collect()
gc.collect()

del a
gc.collect()
gc.collect()
gc.collect()

print wr()
print wr() is None
