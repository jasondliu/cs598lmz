import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() doesn't crash
gc.collect()

# XXX This test isn't very good, but it's a bit tricky to test weakrefs
# XXX in a reliable way.  We should find a better solution.
class Foo(object):
    pass

x = Foo()
x.x = x
w = weakref.ref(x)
x = None
gc.collect()
assert w() is None
gc.collect()
assert w() is None

gc.set_debug(0)
