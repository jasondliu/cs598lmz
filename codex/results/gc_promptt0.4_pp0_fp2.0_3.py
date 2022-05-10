import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A:
    pass
a = A()
a.b = A()
a.b.a = a
w = weakref.ref(a)
print w()
del a
gc.collect()
print w()

# Test gc.get_objects()
class A:
    pass
a = A()
a.b = A()
a.b.a = a
w = weakref.ref(a)
print w()
del a
gc.collect()
print w()

# Test gc.get_referrers()
class A:
    pass
a = A()
a.b = A()
a.b.a = a
w = weakref.ref(a)
print w()
del a
gc.collect()
print w()

# Test gc.get_referents()
class A:
    pass
a = A()
a.b = A()
a.b.a = a
w = weakref.ref(a)
print w()
del a
gc.collect()
print w()

# Test g
