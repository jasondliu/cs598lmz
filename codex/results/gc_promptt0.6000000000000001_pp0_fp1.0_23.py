import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a class containing a weakref to itself
# and a cycle of strong references.
class A:
    pass
a = A()
a.wr = weakref.ref(a)
a.strong = a
del a
gc.collect()
# Test gc.collect() with a class containing a weakref to its class.
class B:
    pass
B.wr = weakref.ref(B)
del B
gc.collect()
# Test gc.collect() with a class containing a weakref to its class,
# which contains a weakref to its class.
class C:
    pass
C.wr = weakref.ref(C)
C.wr2 = weakref.ref(C)
del C
gc.collect()
# Test gc.collect() with a class containing a weakref to its class,
# which contains a weakref to its class, which contains a weakref to
# its class.
class D:
    pass
D.wr = weakref.ref(D)
D.wr2 = weakref.ref(D)
D.wr3 = weakref.
