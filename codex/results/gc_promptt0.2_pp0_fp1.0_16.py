import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    pass

a = A()
b = A()
a.b = b
b.a = a
del a, b
gc.collect()

# Test gc.get_objects()

class A:
    pass

a = A()
b = A()
a.b = b
b.a = a

objects = gc.get_objects()
assert a in objects
assert b in objects

del a, b
gc.collect()

objects = gc.get_objects()
assert a not in objects
assert b not in objects

# Test gc.get_referrers()

class A:
    pass

a = A()
b = A()
a.b = b
b.a = a

referrers = gc.get_referrers(a)
assert a in referrers
assert b in referrers

del a, b
gc.collect()

referrers = gc.get_referrers(a)
assert a not in referrers
assert b not in referrers

