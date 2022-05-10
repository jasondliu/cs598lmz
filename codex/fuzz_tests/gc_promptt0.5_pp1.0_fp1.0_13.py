import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs

class A:
    pass

a = A()
w = weakref.ref(a)
del a
gc.collect()
print w(), w() is None

# Test gc.collect() with cyclic garbage

class A:
    pass

a = A()
a.b = A()
a.b.c = a
del a
gc.collect()

# Test gc.collect() with finalizers

class A:
    pass

a = A()
a.b = A()
a.b.c = a
weakref.ref(a, lambda x: None)
del a
gc.collect()

# Test gc.collect() with uncollectable garbage

class A:
    pass

a = A()
a.b = A()
a.b.c = a
weakref.ref(a)
del a
gc.collect()

class A:
    pass

a = A()
a.b = A()
a.b.c = a
gc.garbage.append(a)
