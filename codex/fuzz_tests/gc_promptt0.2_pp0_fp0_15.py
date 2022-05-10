import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    pass

a = A()
a.b = A()
a.b.a = a

ref = weakref.ref(a)

del a
gc.collect()

print ref() is None

# Test gc.get_referrers()

class A:
    pass

a = A()
a.b = A()
a.b.a = a

ref = weakref.ref(a)

del a
gc.collect()

print ref() is None

print gc.get_referrers(A) == []

# Test gc.get_objects()

class A:
    pass

a = A()
a.b = A()
a.b.a = a

ref = weakref.ref(a)

del a
gc.collect()

print ref() is None

print gc.get_objects() == []

# Test gc.get_referents()

class A:
    pass

a = A()
a.b = A()
