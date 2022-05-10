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

print(ref())

# Test gc.get_referrers()

class A:
    pass

a = A()
a.b = A()
a.b.a = a

ref = weakref.ref(a)

del a
gc.collect()

print(gc.get_referrers(ref))

# Test gc.get_referents()

class A:
    pass

a = A()
a.b = A()
a.b.a = a

ref = weakref.ref(a)

del a
gc.collect()

print(gc.get_referents(ref))

# Test gc.get_objects()

class A:
    pass

a = A()
a.b = A()
a.b.a = a

ref = weakref.
