import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with uncollectable objects.
class X(object):
    def __del__(self):
        del X.instances[0]

A = X()
for i in range(100):
    X.instances = [WeekRef(A)]
    gc.collect()
    print len(gc.garbage)
    gc.garbage.append(None)
del A
erased = gc.collect()
for x in X.instances:
    assert x() is not None
print erased, 'unreachable objects erased from gc.garbage'
