import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with collectable objects that have finalizers and are in a
# reference cycle but have no __del__ method.

class A:
    def __init__(self, x):
        self.b = B(x)
        self.c = C(x)
        self.a = self

class B:
    def __init__(self, x):
        self.x = x

class C:
    def __init__(self, x):
        self.x = x

    def __del__(self):
        pass

# Weakrefs to the objetcs should come in handy
objs = []

for i in range(20):
    a = A(i)
    objs.append(weakref.ref(a))

# Execute gc.collect() and check if the objects have been collected.
collectable = gc.collect()
for i, a in enumerate(objs):
    assert a() is None, i

collectable = gc.collect()
for i, a in enumerate(objs):
    assert a() is None
