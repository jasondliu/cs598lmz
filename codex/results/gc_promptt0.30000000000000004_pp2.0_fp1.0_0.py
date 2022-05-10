import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A:
    pass
a = A()
a.b = A()
a.b.a = a
a.b.b = a.b
del a
gc.collect()
# Test weakref.ref()
class A:
    pass
a = A()
a.b = A()
a.b.a = a
a.b.b = a.b
r = weakref.ref(a)
del a
gc.collect()
# Test weakref.proxy()
class A:
    pass
a = A()
a.b = A()
a.b.a = a
a.b.b = a.b
r = weakref.proxy(a)
del a
gc.collect()
