import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    pass
a = A()
b = weakref.ref(a)

print(gc.collect())
print(gc.garbage)
del a
print(gc.collect())
print(gc.garbage)
print(b())
print(gc.garbage)

# Test gc.get_referents()

x = 1
print(gc.get_referents(x))
del x
print(gc.collect())
print(gc.garbage)

# Test gc.get_referrers()

x = 1
print(gc.get_referrers(x))
del x
print(gc.collect())
print(gc.garbage)

# Test gc.get_objects()

def f():
    pass
x = 1
print(gc.get_objects())
del f, x
print(gc.collect())
print(gc.garbage)

# Test gc.is_tracked()

x = 1
print(gc.is_tracked(x))
del x
print
