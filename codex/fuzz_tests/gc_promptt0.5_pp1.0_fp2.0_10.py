import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

# Create some objects
class Foo: pass
f = Foo()
f2 = Foo()
f2.f = f

# Create some cycles
c = []
c.append(c)

# Create some weakrefs
l = []
w = weakref.ref(l)

# Create some uncollectable objects
def create_uncollectable():
    class Uncollectable:
        def __del__(self):
            pass
    u = Uncollectable()
    u.u = u
    return u
u = create_uncollectable()

# Create some uncollectable cycles
def create_uncollectable():
    class Uncollectable:
        def __del__(self):
            pass
    u = Uncollectable()
    def f():
        u.u = u
    u.f = f
    return u
u2 = create_uncollectable()

# Create some finalizers
def create_finalizer():
    class Finalizer:
        def __del__(self):
            pass
    f = Finalizer()

