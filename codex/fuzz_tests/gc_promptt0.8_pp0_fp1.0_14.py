import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() returns 0 when everything is collected
# (due to GCFLAG_COLLECTABLE set only on collectable objects)

class C:
    pass

def f():
    o = C()
    r = weakref.ref(o)
    del o
    return r

def callback(ignore):
    print "callback"

for i in range(5):
    r = f()
    r.callback = callback
    # this should do nothing because the object is not tracked
    # by the GC (due to having no __del__ method)
    gc.collect()
    print "cycle", i

# This should do nothing because everything is collectable.
# The callback should never be called.
gc.collect()

# Exercise the code path for unreachable but not yet collected objects.
class C1(object):
    def __del__(self):
        print "C1 __del__"

class C2(object):
    def __new__(self):
        print "C2 __new__"
        return object.__new__(object)

r1 = weakref
