import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() on a weakref.

class Dummy:
    pass

obj = Dummy()
obj.x = 1
w = weakref.ref(obj)
del obj

del attr

gc.collect()
print 'after garbage collection:'
for r in gc.garbage:
    print r
