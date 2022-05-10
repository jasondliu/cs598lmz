import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs

class A:
    pass

a = A()
b = A()
a.b = b
b.a = a

w = weakref.ref(a)
del a
gc.collect()
assert w() is None
assert gc.collect() == 0

w = weakref.ref(b)
del b
gc.collect()
assert w() is None
assert gc.collect() == 0

# Test gc.collect() with a cyclic garbage object

class A:
    pass

a = A()
a.a = a

w = weakref.ref(a)
del a
gc.collect()
assert w() is None
assert gc.collect() == 0

# Test gc.collect() with a cyclic garbage object and a weakref

class A:
    pass

a = A()
a.a = a

w = weakref.ref(a)
del a
gc.collect()
assert w() is None
assert gc.collect() == 0

# Test gc.collect()
