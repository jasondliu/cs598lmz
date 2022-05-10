import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
gc.collect()
gc.collect()

class A:
    pass

a = A()
b = A()

a.b = b
b.a = a
del a
del b
gc.collect()

gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
gc.collect()
gc.collect()

class B:
    pass

b = B()
b.b = b

gc.collect()

gc.set_debug(gc.DEBUG_SAVEALL)
gc.collect()
gc.collect()

gc.collect()

gc.set_debug(gc.DEBUG_LEAK)
gc.collect()
gc.collect()

gc.collect()

gc.set_debug(gc.DEBUG_STATS)
gc.collect()
gc.collect()

gc.collect()

class C:
    pass

c = C()
c.c = c
del c
gc.collect()

gc.set_debug(gc.DEBUG_INSTANCES)
gc.collect()
