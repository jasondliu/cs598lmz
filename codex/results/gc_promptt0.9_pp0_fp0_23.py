import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() on weakrefs, moving weakref'd objects around
class Foo:
    def __del__(self):
        self.bar.doomed = True

class Bar(object):
    pass

# Create a loop, from f to b to f.
b = Bar()
f = Foo()
f.bar = b
b.foo = f

# Create a weakref to b.
w = weakref.ref(b)

# Break the loop.
del f.bar
del b.foo

# Clear references to b and f in this frame.
b = None
f = None

# Sanity check to ensure that b and f don't exist.
# When called later, this should invoke the __del__ method of Foo.
w().foo

gc.collect()

# w is empty and alive (but the object is not, of course).
assert w() is None
assert w() is None
assert gc.garbage[-1].doomed

# weakref and weakproxy subclasses
import gc
gc.collect()

class MyRef(weakref.
