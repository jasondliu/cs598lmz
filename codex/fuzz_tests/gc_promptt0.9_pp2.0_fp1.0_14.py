import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
# Cycle
class A:
    pass
a = A()
a.someA = A()
a.someA.someB = a.someB = B()
del a, A
gc.collect()
print gc.garbage
print "#" * 79
# Weak references
class A:
    pass
a = A()
weakref.ref(a)
del a
gc.collect()
print gc.garbage
print "#" * 79
# Garbage detection with weakrefs
class A:
    pass
a = A()
a.b = A()
a.b.c = A()
a.b.c.d = A()
a.b.c.d.e = A()
a.b.c.d.e.f = a
del a
del A
gc.collect()
print gc.garbage
print "#" * 79
