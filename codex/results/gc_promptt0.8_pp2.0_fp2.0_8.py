import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
def f():
    gc.collect()
    gc.collect()

# Test weak references
import weakref
def f():
    # Testing weak references
    class Foo(object):
        def __init__(self, i):
            self.i = i
        def __repr__(self):
            return "<Foo %r>" % self.i

    f = Foo(42)
    f.bar = lambda: f
    r = weakref.ref(f)
    # Make sure the weak reference is removed from the key:value
    # pair before the value is collected.  A previous version
    # collected the value, then removed the weak reference from
    # the key:value pair, then decremented the reference count on
    # the value.  The decrement should have returned zero, but
    # instead returned 1 because the weak reference was still in
    # the key:value pair.
    f = None
    gc.collect()
    #print(r())

    # Testing cyclic gc
    f = Foo(43)
    r = weakref.ref(
