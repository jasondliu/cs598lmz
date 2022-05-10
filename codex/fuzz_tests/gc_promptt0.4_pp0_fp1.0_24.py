import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback that creates a new reference cycle.
# This used to crash Python.

def callback(wr):
    # Create a new reference cycle.
    l = [wr]
    l.append(l)

class Foo:
    pass

f = Foo()
wr = weakref.ref(f, callback)
del f
gc.collect()
print "OK"
