import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    def __del__(self):
        print "deleting Foo"

f = Foo()

# This should trigger collection
c = weakref.ref(f)
f = None
gc.collect()

# This should not trigger collection
c = weakref.ref(f)
gc.collect()

# This should trigger collection
c = weakref.ref(f)
del f
gc.collect()

# This should trigger collection
c = weakref.ref(f)
del c
gc.collect()

# This should trigger collection
c = weakref.ref(f)
c = None
gc.collect()

# This should trigger collection
c = weakref.ref(f)
c = None
gc.collect()

# This should not trigger collection
c = weakref.ref(f)
gc.collect()

# This should trigger collection
c = weakref.ref(f)
del f
gc.collect()

# This should trigger collection
c = weakref.ref(f)
del c
gc.collect()

