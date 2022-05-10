import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() when the deallocator is the only
# thing holding an object alive.

class MyObj:
    def __init__(self, aObj):
        self.a = aObj

    def __del__(self):
        self.a.x = 1

N = 100
objs = []
a = MyObj(None)
a.x = 0
for i in range(N):
    o = MyObj(a)
    o.x = 0
    objs.append(o)
    # At this point, "a" prevents "o" from being freed.

# Force a collection.  Since "a" has no references
# to "i", "a" is freed, which allows o.__del__ to run,
# which sets a.x = 1, which creates a cycle.  Hence
# the collect passes over the whole cycle twice.
gc.collect()
del objs
del a
gc.collect()
try:
    gc.garbage[0]()
except (TypeError, AttributeError, IndexError):
    pass
else:
    print('
