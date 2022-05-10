import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    pass

a = A()
a.b = A()
a.b.a = a

ref_a = weakref.ref(a)

del a
gc.collect()

print ref_a() is None

# Test gc.garbage

class A:
    pass

a = A()
a.b = A()
a.b.a = a

del a

gc.collect()

print len(gc.garbage) == 1

# Test gc.get_count()

print gc.get_count() == (0, 0, 0)

a = []
print gc.get_count() == (1, 0, 0)

b = []
b.append(b)
print gc.get_count() == (1, 1, 0)

del a, b
gc.collect()

print gc.get_count() == (0, 0, 0)

# Test gc.get_threshold()

print gc.get_threshold() == (
