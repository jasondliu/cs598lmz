import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs

class Foo(object):
    pass

f = Foo()
r = weakref.ref(f)

print "collecting..."
gc.collect()
print "done."

print r() is f

del f
print r() is None

print "collecting..."
gc.collect()
print "done."
