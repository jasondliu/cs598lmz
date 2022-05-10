import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A:
    pass

a = A()
a.x = A()
a.y = A()
a.x.b = a
a.y.b = a

print(gc.collect())
print(gc.collect())
print(gc.collect())

del a

print(gc.collect())
print(gc.collect())
print(gc.collect())

# Test gc.garbage
a = A()
a.x = A()
a.y = A()
a.x.b = a
a.y.b = a

print(a)
print(a.x)
print(a.y)
print(a.x.b)
print(a.y.b)

del a.x
del a.y
del a

print(gc.collect())
print(gc.garbage)

# Test gc.get_objects()
print(gc.get_objects())

# Test gc.get_referrers()
print(gc.get_referrers(gc))

# Test g
