import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect with a cycle of weakrefs.

class X:
    pass

x = X()
y = X()
x.foo = y
y.bar = x

w = weakref.ref(x)
del x
del y
gc.collect()
assert w() is None

gc.set_debug(0)

# Test gc.collect with a cycle of weakrefs that are not collectable.

gc.set_debug(gc.DEBUG_UNCOLLECTABLE)

class A:
    def __init__(self, b):
        self.b = b

a = A(None)
b = A(a)
a.b = b

wa = weakref.ref(a)
wb = weakref.ref(b)
del a
del b
gc.collect()
assert wa() is not None
assert wb() is not None

gc.set_debug(0)

# Test gc.collect with a cycle of weakrefs that are not collectable,
# but that we break the cycle on.

gc.set_debug(
