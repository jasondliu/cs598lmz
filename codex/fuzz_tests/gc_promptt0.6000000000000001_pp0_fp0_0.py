import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

class A:
    pass

a = A()
a.b = A()
a.b.a = a
del a
gc.collect()

a = A()
a.b = A()
a.b.a = a
del a.b
gc.collect()

a = A()
a.b = A()
a.b.a = a
del a.b.a
del a
gc.collect()

a = A()
a.b = A()
a.b.a = a
a.b = None
del a
gc.collect()

a = A()
a.b = A()
a.b.a = a
a.b = None
del a.b
gc.collect()

a = A()
a.b = A()
a.b.a = a
a.b = None
del a.b.a
del a
gc.collect()

a = A()
a.b = A()
a.b.a = a
a.b = None
del a.
